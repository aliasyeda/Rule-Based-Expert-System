# ========== SIMPLE RULE ENGINE - NO LIBRARIES NEEDED ==========
# Works with Python 3.14 and any version!

class SimpleExpertSystem:
    def __init__(self):
        self.facts = {}           # What we know
        self.rules = []           # IF-THEN rules
        self.reasoning_path = []  # Log of inferences
        self.inferred = set()     # Prevent infinite loops
    
    def add_fact(self, key, value):
        """Add a fact to knowledge base"""
        self.facts[key] = value
        self.reasoning_path.append(f"📌 Added fact: {key} = {value}")
    
    def add_rule(self, conditions, conclusion, condition_func=None):
        """
        Add a rule
        conditions: list of required facts
        conclusion: what to infer
        condition_func: optional custom function for complex logic
        """
        self.rules.append({
            'conditions': conditions,
            'conclusion': conclusion,
            'func': condition_func
        })
        self.reasoning_path.append(f"📝 Added rule: IF {conditions} THEN {conclusion}")
    
    def check_conditions(self, conditions, custom_func=None):
        """Check if all conditions are met"""
        # Check basic conditions (all must be True)
        for cond in conditions:
            if cond not in self.facts or not self.facts[cond]:
                return False
        
        # Check custom function if provided
        if custom_func and not custom_func(self.facts):
            return False
        
        return True
    
    def forward_chain(self):
        """Run forward chaining inference"""
        print("\n" + "="*60)
        print("🔍 STARTING FORWARD CHAINING")
        print("="*60)
        
        new_fact_added = True
        iteration = 0
        
        while new_fact_added:
            iteration += 1
            new_fact_added = False
            
            print(f"\n📊 Iteration {iteration}:")
            
            for rule in self.rules:
                # Skip if already inferred
                conclusion = rule['conclusion']
                if conclusion in self.inferred:
                    continue
                
                # Check if rule conditions are met
                if self.check_conditions(rule['conditions'], rule.get('func')):
                    # Add new fact
                    self.facts[conclusion] = True
                    self.inferred.add(conclusion)
                    
                    # Log the inference
                    step = f"  🔥 Rule fired: IF {rule['conditions']} THEN {conclusion}"
                    print(step)
                    self.reasoning_path.append(step)
                    
                    new_fact_added = True
        
        print("\n✅ Inference complete!")
        return self.facts
    
    def explain(self):
        """Show complete reasoning path"""
        print("\n" + "="*60)
        print("📋 COMPLETE REASONING PATH")
        print("="*60)
        for i, step in enumerate(self.reasoning_path, 1):
            print(f"{i}. {step}")
    
    def get_diagnosis(self):
        """Get all diagnosis results"""
        diagnoses = [fact for fact in self.facts if 'diagnosis' in fact]
        actions = [fact for fact in self.facts if 'action' in fact]
        
        print("\n" + "="*60)
        print("💡 FINAL RESULTS")
        print("="*60)
        
        if diagnoses:
            print("✅ DIAGNOSES:")
            for d in diagnoses:
                print(f"   - {d.replace('_', ' ').title()}")
        else:
            print("❌ No specific diagnosis yet")
        
        if actions:
            print("\n📋 RECOMMENDED ACTIONS:")
            for a in actions:
                print(f"   - {self.facts[a]}")
    
    def reset(self):
        """Reset for new session"""
        self.facts = {}
        self.reasoning_path = []
        self.inferred = set()

# ========== TECH SUPPORT EXPERT SYSTEM ==========

def run_tech_support():
    """Main program for tech support diagnosis"""
    
    print("="*60)
    print("🤖 TECH SUPPORT EXPERT SYSTEM")
    print("="*60)
    print("Describe your computer problem")
    print("(type 'exit' to quit)")
    print("-"*60)
    
    while True:
        # Create new engine instance for each query
        engine = SimpleExpertSystem()
        
        # Get user input
        user_input = input("\n❓ What's the problem? ").lower()
        
        if user_input == 'exit':
            print("\n👋 Goodbye! Thanks for using Tech Support.")
            break
        
        print("\n🔍 Analyzing...")
        
        # ===== ADD FACTS BASED ON USER INPUT =====
        
        # Check for power issues
        if any(word in user_input for word in ['power', 'turn on', 'start', 'dead', 'no light']):
            engine.add_fact('power_issue', True)
        
        # Check for internet issues
        if any(word in user_input for word in ['internet', 'wifi', 'network', 'connect', 'online']):
            engine.add_fact('network_issue', True)
        
        # Check for performance issues
        if any(word in user_input for word in ['slow', 'lag', 'freeze', 'crash', 'unresponsive']):
            engine.add_fact('performance_issue', True)
        
        # Check for display issues
        if any(word in user_input for word in ['screen', 'display', 'monitor', 'blank', 'black']):
            engine.add_fact('display_issue', True)
        
        # Check for peripheral issues
        if any(word in user_input for word in ['mouse', 'keyboard', 'usb', 'printer', 'peripheral']):
            engine.add_fact('peripheral_issue', True)
        
        # ===== ADD RULES (IF-THEN statements) =====
        
        # Rule 1: Power issue diagnosis
        engine.add_rule(
            conditions=['power_issue'],
            conclusion='diagnosis_power_problem'
        )
        
        # Rule 2: Network issue diagnosis  
        engine.add_rule(
            conditions=['network_issue'],
            conclusion='diagnosis_network_problem'
        )
        
        # Rule 3: Performance issue diagnosis
        engine.add_rule(
            conditions=['performance_issue'],
            conclusion='diagnosis_performance_problem'
        )
        
        # Rule 4: Display issue diagnosis
        engine.add_rule(
            conditions=['display_issue'],
            conclusion='diagnosis_display_problem'
        )
        
        # Rule 5: Peripheral issue diagnosis
        engine.add_rule(
            conditions=['peripheral_issue'],
            conclusion='diagnosis_peripheral_problem'
        )
        
        # Rule 6: Multiple issues (chaining example)
        engine.add_rule(
            conditions=['power_issue', 'display_issue'],
            conclusion='diagnosis_power_supply_failure'
        )
        
        # Rule 7: Action for power issue
        engine.add_rule(
            conditions=['diagnosis_power_problem'],
            conclusion='action_check_power_cable'
        )
        if 'diagnosis_power_problem' in engine.facts:
            engine.facts['action_check_power_cable'] = "Check power cable and try different outlet"
        
        # Rule 8: Action for network issue
        engine.add_rule(
            conditions=['diagnosis_network_problem'],
            conclusion='action_restart_router'
        )
        if 'diagnosis_network_problem' in engine.facts:
            engine.facts['action_restart_router'] = "Restart router/modem and check WiFi settings"
        
        # Rule 9: Action for performance issue
        engine.add_rule(
            conditions=['diagnosis_performance_problem'],
            conclusion='action_clean_system'
        )
        if 'diagnosis_performance_problem' in engine.facts:
            engine.facts['action_clean_system'] = "Close unused programs and restart computer"
        
        # Rule 10: Action for display issue
        engine.add_rule(
            conditions=['diagnosis_display_problem'],
            conclusion='action_check_cables'
        )
        if 'diagnosis_display_problem' in engine.facts:
            engine.facts['action_check_cables'] = "Check video cables and try different port"
        
        # Rule 11: Action for peripheral issue
        engine.add_rule(
            conditions=['diagnosis_peripheral_problem'],
            conclusion='action_reconnect_device'
        )
        if 'diagnosis_peripheral_problem' in engine.facts:
            engine.facts['action_reconnect_device'] = "Unplug and reconnect device, try different USB port"
        
        # ===== RUN INFERENCE =====
        
        if len(engine.facts) > 0:
            # Run forward chaining
            engine.forward_chain()
            
            # Show results
            engine.get_diagnosis()
            
            # Show reasoning path (impressive for interview!)
            print("\n" + "="*60)
            print("🧠 SHOW REASONING PATH? (yes/no)")
            show = input().lower()
            if show == 'yes':
                engine.explain()
        else:
            print("\n❓ I couldn't identify the problem. Please describe in more detail.")
            print("Try using words like: power, internet, slow, screen, or USB")

# ========== RUN THE PROGRAM ==========
if __name__ == "__main__":
    run_tech_support()