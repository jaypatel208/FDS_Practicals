import pandas as pd
import os

# Function to input data from user
def get_input_data():
    data = {
        "City": [],
        "Temperature (°C)": [],
        "Population Density (people/km²)": [],
        "Tourist Attractions": [],
        "Public Transport Index": []
    }
    
    while True:
        city = input("Enter City Name: ")
        temperature = float(input(f"Enter average temperature for {city} (in °C): "))
        pop_density = float(input(f"Enter population density of {city} (people/km²): "))
        attractions = int(input(f"Enter number of tourist attractions in {city}: "))
        transport_index = int(input(f"Enter public transport index (1-100) for {city}: "))

        # Append input to data
        data["City"].append(city)
        data["Temperature (°C)"].append(temperature)
        data["Population Density (people/km²)"].append(pop_density)
        data["Tourist Attractions"].append(attractions)
        data["Public Transport Index"].append(transport_index)

        # Ask user if they want to continue
        cont = input("Do you want to add more cities? (yes/no): ").lower()
        if cont != 'yes':
            break
            
    return data

# Function to save data into an Excel file
def save_to_excel(data, filename="city_data.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"\nData successfully saved to {filename}")

# Function to display data in tabular format
def display_data(filename="city_data.xlsx"):
    if os.path.exists(filename):
        df = pd.read_excel(filename)
        print("\nSaved Data:\n")
        print(df)
    else:
        print(f"{filename} does not exist. Please save data first.")

# Main program logic
def main():
    data = get_input_data()
    save_to_excel(data)
    display_data()

if __name__ == "__main__":
    main()