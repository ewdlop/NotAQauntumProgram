#!/usr/bin/env python3
"""
Examples for 心物盒一 (Mind-Matter Box One)

Various examples demonstrating different aspects of the Mind-Matter Box.
"""

from mind_matter_box import MindMatterBox
import time


def example_basic_usage():
    """Basic usage example."""
    print("=== Basic Usage Example ===")
    
    box = MindMatterBox("Example Box")
    print(f"Created box: {box.name}")
    
    # Put in superposition and observe
    box.enter_superposition()
    result = box.observe("curious")
    
    print(f"Observed state: {result['physical_state']} / {result['mental_state']}")
    print()


def example_observer_intent_effects():
    """Demonstrate how observer intent affects outcomes."""
    print("=== Observer Intent Effects ===")
    
    box = MindMatterBox("Intent Box")
    
    intents = ["peaceful", "anxious", "curious"]
    
    for intent in intents:
        box.enter_superposition()
        result = box.observe(intent)
        print(f"{intent.capitalize()} observer sees: {result['physical_state']} matter, {result['mental_state']} mind")
    
    print()


def example_meditation_insights():
    """Show how meditation generates different insights."""
    print("=== Meditation Insights ===")
    
    box = MindMatterBox("Wisdom Box")
    
    print("Collecting insights through meditation:")
    for i in range(3):
        insight = box.meditate(0.01)  # Quick meditation for demo
        print(f"  {i+1}. {insight}")
    
    print()


def example_box_lifecycle():
    """Demonstrate the full lifecycle of a box."""
    print("=== Box Lifecycle ===")
    
    box = MindMatterBox("Lifecycle Box")
    
    print("1. Initial state:")
    print(f"   {box.get_status()}")
    
    print("\n2. Enter superposition:")
    box.enter_superposition()
    print(f"   Observation state: {box.observation_state.value}")
    
    print("\n3. First observation:")
    result = box.observe("peaceful")
    print(f"   Result: {result['physical_state']} / {result['mental_state']}")
    
    print("\n4. Meditation:")
    insight = box.meditate(0.01)
    print(f"   Insight: {insight}")
    
    print("\n5. Final state:")
    final_status = box.get_status()
    print(f"   Age: {final_status['age_seconds']:.4f} seconds")
    print(f"   State: {final_status['observation_state']}")
    
    print()


def example_multiple_boxes():
    """Demonstrate multiple boxes with different characteristics."""
    print("=== Multiple Boxes ===")
    
    boxes = [
        MindMatterBox("Alpha Box"),
        MindMatterBox("Beta Box"), 
        MindMatterBox("Gamma Box")
    ]
    
    # Set each box to superposition
    for box in boxes:
        box.enter_superposition()
    
    # Observe each with different intent
    intents = ["peaceful", "curious", "anxious"]
    
    for box, intent in zip(boxes, intents):
        result = box.observe(intent)
        print(f"{box.name} ({intent}): {result['physical_state']} / {result['mental_state']}")
    
    print()


if __name__ == "__main__":
    print("心物盒一 (Mind-Matter Box One) - Examples\n")
    
    example_basic_usage()
    example_observer_intent_effects()
    example_meditation_insights()
    example_box_lifecycle()
    example_multiple_boxes()
    
    print("Examples complete. Try creating your own Mind-Matter Box!")