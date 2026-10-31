
import pytest
from shipping_quote import process_shipments, monitor_container_pressures


# 1. Input validation
def test_invalid_shipments_type():
    with pytest.raises(ValueError):
        process_shipments("invalid", 10.0)


def test_negative_handling_fee():
    with pytest.raises(ValueError):
        process_shipments([], -5.0)


# 2. Transport mode and weight calculations
def test_air_shipment():
    shipments = [{
        "manifest_approved": True,
        "mode": "air",
        "packages": [{"weight_kg": 10, "is_hazmat": False}]
    }]
    result = process_shipments(shipments, 5.0)
    assert result == {"total_quote": 125.0, "status": "CLEARED"}


def test_ground_heavy_shipment():
    shipments = [{
        "manifest_approved": True,
        "mode": "ground",
        "packages": [{"weight_kg": 40, "is_hazmat": False}]
    }]
    result = process_shipments(shipments, 5.0)
    assert result == {"total_quote": 245.0, "status": "CLEARED"}


def test_ground_normal_shipment():
    shipments = [{
        "manifest_approved": True,
        "mode": "ground",
        "packages": [{"weight_kg": 10, "is_hazmat": False}]
    }]
    result = process_shipments(shipments, 5.0)
    assert result == {"total_quote": 45.0, "status": "CLEARED"}


def test_unsupported_transport_mode():
    shipments = [{
        "manifest_approved": True,
        "mode": "sea",
        "packages": [{"weight_kg": 10}]
    }]
    result = process_shipments(shipments, 5.0)
    assert result == {"total_quote": 0.0, "status": "NO_CARGO"}


# 3. Manifest approval
def test_unapproved_manifest():
    shipments = [{
        "manifest_approved": False,
        "mode": "air",
        "packages": [{"weight_kg": 10}]
    }]
    result = process_shipments(shipments, 5.0)
    assert result == {"total_quote": 0.0, "status": "NO_CARGO"}


# 4. Package validation
def test_zero_and_negative_weights():
    shipments = [{
        "manifest_approved": True,
        "mode": "ground",
        "packages": [
            {"weight_kg": 0},
            {"weight_kg": -5}
        ]
    }]
    result = process_shipments(shipments, 5.0)
    assert result == {"total_quote": 5.0, "status": "CLEARED"}


# 5. Hazardous material handling
def test_hazmat_non_fragile():
    shipments = [{
        "manifest_approved": True,
        "mode": "ground",
        "is_fragile": False,
        "packages": [{"weight_kg": 10, "is_hazmat": True}]
    }]
    result = process_shipments(shipments, 5.0)
    assert result == {"total_quote": 55.0, "status": "CLEARED"}


def test_hazmat_fragile():
    shipments = [{
        "manifest_approved": True,
        "mode": "ground",
        "is_fragile": True,
        "packages": [
            {"weight_kg": 10, "is_hazmat": True},
            {"weight_kg": 20, "is_hazmat": False}
        ]
    }]
    result = process_shipments(shipments, 5.0)
    assert result == {"total_quote": 0.0, "status": "NO_CARGO"}


# 6. Express priority
def test_express_priority():
    shipments = [{
        "manifest_approved": True,
        "mode": "air",
        "express_priority": True,
        "packages": [{"weight_kg": 2, "is_hazmat": False}]
    }]
    result = process_shipments(shipments, 4.0)
    assert result == {"total_quote": 35.0, "status": "CLEARED"}


# 7. Rejected parcels and review status
def test_flagged_review():
    shipments = [{
        "manifest_approved": True,
        "mode": "ground",
        "packages": [
            {"weight_kg": 0},
            {"weight_kg": -1},
            {"weight_kg": 0},
            {"weight_kg": -2}
        ]
    }]
    result = process_shipments(shipments, 0.0)
    assert result == {"total_quote": 0.0, "status": "FLAGGED_REVIEW"}


# 8. No cargo
def test_no_cargo():
    result = process_shipments([], 10.0)
    assert result == {"total_quote": 0.0, "status": "NO_CARGO"}


# 9. Container pressure monitoring
def test_empty_pressure_logs():
    assert monitor_container_pressures([]) == "NO_DATA"


def test_leak_detected():
    pressure_logs = [
        [15.0, 13.0, 12.0]
    ]
    assert monitor_container_pressures(pressure_logs) == "LEAK_DETECTED"


def test_stable_pressure():
    pressure_logs = [
        [15.0, 13.0, 15.0, 13.0],
        [16.0, 15.0, 14.5]
    ]
    assert monitor_container_pressures(pressure_logs) == "STABLE"
