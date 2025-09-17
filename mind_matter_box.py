#!/usr/bin/env python3
"""
心物盒一 (Mind-Matter Box One)

A philosophical thought experiment implementation that explores the relationship
between consciousness (mind) and physical reality (matter) in a box-like system.

This is NOT a quantum program, despite dealing with observation and state.
"""

import random
import time
from enum import Enum
from typing import Optional


class ObservationState(Enum):
    """Possible states of observation."""
    UNOBSERVED = "unobserved"
    OBSERVED = "observed"
    SUPERPOSITION = "superposition"


class MindMatterBox:
    """
    The Mind-Matter Box (心物盒一) represents a philosophical thought experiment
    about the relationship between consciousness and physical reality.
    
    Unlike Schrödinger's cat, this explores how mental states might influence
    or correlate with physical states in a contained system.
    """
    
    def __init__(self, name: str = "Box One"):
        self.name = name
        self.physical_state: str = "undefined"
        self.mental_state: str = "undefined"
        self.observation_state: ObservationState = ObservationState.UNOBSERVED
        self.creation_time = time.time()
        self.last_interaction = None
        
    def observe(self, observer_intent: str = "curious") -> dict:
        """
        Observe the box, which collapses the superposition of mind-matter states.
        
        Args:
            observer_intent: The mental state/intent of the observer
            
        Returns:
            Dictionary containing the observed states
        """
        self.observation_state = ObservationState.OBSERVED
        self.last_interaction = time.time()
        
        # The observation intent influences the outcome (mind affecting matter)
        if observer_intent == "peaceful":
            self.physical_state = "harmonious"
            self.mental_state = "serene"
        elif observer_intent == "curious":
            self.physical_state = "dynamic"
            self.mental_state = "inquisitive"
        elif observer_intent == "anxious":
            self.physical_state = "chaotic"
            self.mental_state = "turbulent"
        else:
            # Random state for neutral observation
            physical_options = ["stable", "fluctuating", "resonant"]
            mental_options = ["contemplative", "focused", "wandering"]
            self.physical_state = random.choice(physical_options)
            self.mental_state = random.choice(mental_options)
            
        return {
            "physical_state": self.physical_state,
            "mental_state": self.mental_state,
            "observation_time": self.last_interaction,
            "observer_intent": observer_intent
        }
    
    def enter_superposition(self):
        """Reset the box to an unobserved superposition state."""
        self.observation_state = ObservationState.SUPERPOSITION
        self.physical_state = "all possible states"
        self.mental_state = "all possible thoughts"
        
    def get_status(self) -> dict:
        """Get the current status of the mind-matter box."""
        return {
            "name": self.name,
            "physical_state": self.physical_state,
            "mental_state": self.mental_state,
            "observation_state": self.observation_state.value,
            "age_seconds": time.time() - self.creation_time,
            "last_interaction": self.last_interaction
        }
    
    def meditate(self, duration: float = 1.0) -> str:
        """
        Allow the box to exist in contemplative state for a period.
        
        Args:
            duration: Time in seconds to meditate
            
        Returns:
            Insight gained from meditation
        """
        time.sleep(duration)
        
        insights = [
            "Mind and matter are two sides of the same coin",
            "Observation changes both observer and observed",
            "Consciousness shapes reality through intention",
            "The boundary between mind and matter is an illusion",
            "Awareness is the bridge between thought and form"
        ]
        
        return random.choice(insights)


def demonstrate_mind_matter_box():
    """Demonstration of the Mind-Matter Box concept."""
    print("=== 心物盒一 (Mind-Matter Box One) Demonstration ===\n")
    
    # Create the box
    box = MindMatterBox("心物盒一")
    print(f"Created: {box.name}")
    print(f"Initial status: {box.get_status()}\n")
    
    # Enter superposition
    box.enter_superposition()
    print("Box enters superposition state...")
    print(f"Current state: {box.get_status()}\n")
    
    # Observe with different intents
    intents = ["curious", "peaceful", "anxious", "neutral"]
    
    for intent in intents:
        print(f"Observing with '{intent}' intent:")
        result = box.observe(intent)
        print(f"  Physical state: {result['physical_state']}")
        print(f"  Mental state: {result['mental_state']}")
        print()
        
        # Reset to superposition for next observation
        box.enter_superposition()
    
    # Meditation
    print("Box enters meditation...")
    insight = box.meditate(0.1)  # Short duration for demo
    print(f"Insight gained: '{insight}'\n")
    
    # Final status
    print("Final status:")
    print(box.get_status())


if __name__ == "__main__":
    demonstrate_mind_matter_box()