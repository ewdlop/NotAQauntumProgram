#!/usr/bin/env python3
"""
Tests for 心物盒一 (Mind-Matter Box One)

Simple tests to verify the Mind-Matter Box functionality.
"""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mind_matter_box import MindMatterBox, ObservationState


def test_box_creation():
    """Test that a box can be created with proper initial state."""
    box = MindMatterBox("Test Box")
    assert box.name == "Test Box"
    assert box.physical_state == "undefined"
    assert box.mental_state == "undefined"
    assert box.observation_state == ObservationState.UNOBSERVED
    print("✓ Box creation test passed")


def test_superposition():
    """Test that box can enter superposition state."""
    box = MindMatterBox()
    box.enter_superposition()
    assert box.observation_state == ObservationState.SUPERPOSITION
    assert box.physical_state == "all possible states"
    assert box.mental_state == "all possible thoughts"
    print("✓ Superposition test passed")


def test_observation():
    """Test that observation changes the box state."""
    box = MindMatterBox()
    box.enter_superposition()
    
    # Test peaceful observation
    result = box.observe("peaceful")
    assert box.observation_state == ObservationState.OBSERVED
    assert result["physical_state"] == "harmonious"
    assert result["mental_state"] == "serene"
    assert result["observer_intent"] == "peaceful"
    
    # Reset and test curious observation
    box.enter_superposition()
    result = box.observe("curious")
    assert result["physical_state"] == "dynamic"
    assert result["mental_state"] == "inquisitive"
    
    print("✓ Observation test passed")


def test_meditation():
    """Test that meditation returns insights."""
    box = MindMatterBox()
    insight = box.meditate(0.01)  # Very short meditation for testing
    assert isinstance(insight, str)
    assert len(insight) > 0
    print("✓ Meditation test passed")


def test_status():
    """Test that status returns proper information."""
    box = MindMatterBox("Status Test")
    status = box.get_status()
    
    required_keys = ["name", "physical_state", "mental_state", 
                    "observation_state", "age_seconds", "last_interaction"]
    
    for key in required_keys:
        assert key in status
    
    assert status["name"] == "Status Test"
    print("✓ Status test passed")


def run_all_tests():
    """Run all tests for the Mind-Matter Box."""
    print("Running Mind-Matter Box tests...\n")
    
    try:
        test_box_creation()
        test_superposition()
        test_observation()
        test_meditation()
        test_status()
        
        print("\n🎉 All tests passed! The 心物盒一 implementation is working correctly.")
        return True
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return False
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)