import simpy

def hair_wash_simulation(env, hair_type, conditioner_type, conditioner_freq, clarifying_freq, other_factors, climate_factors):
    while True:
        wash_frequency = calculate_wash_frequency(hair_type, other_factors, climate_factors)
        yield env.timeout(wash_frequency)
        
        print(f"Day {env.now}: Wash hair with regular shampoo.")
        
        if env.now % clarifying_freq == 0:
            print(f"Day {env.now}: Use clarifying shampoo.")
        if env.now % conditioner_freq == 0:
            print(f"Day {env.now}: Use {conditioner_type} conditioner.")

def calculate_wash_frequency(hair_type, other_factors, climate_factors):
    # Simplified logic for demonstration purposes
    base_frequency = {
        'straight': 3,
        'wavy': 4,
        'curly': 5,
        'coily': 6
    }.get(hair_type, 4) #default
    
    # Adjust based on other factors and climate
    adjusted_frequency = base_frequency - climate_factors.get('humidity', 0)
    return max(1, adjusted_frequency)  # Ensure at least 1 day between washes

# Initialize the simulation environment
env = simpy.Environment()
env.process(hair_wash_simulation(env, 'curly', 'moisturizing', 3, 7, {}, {'humidity': 1}))
env.run(until=30)  # Run the simulation for 30 days
