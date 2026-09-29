def convert_temperature(value, unit):
    if unit.upper() == "C":
        return (value * 9/5) + 32 
    elif unit.upper() == "F":
        return (value - 32) * 5/9  
    else:
        print("Tidak Ada Unit")

print("======== KONVERSI SUHU ========")

input_suhu = float(input("Masukkan nilai suhu:"))
unit = input("Masukkan satuan suhu ('C' untuk Celcius atau 'F' untuk Fahrenheit): ")
konversi = convert_temperature(input_suhu, unit)
if unit.upper() == 'C':
    print(f"{input_suhu}°C = {konversi}°F")
elif unit.upper() == 'F':
    print(f"{input_suhu}°F = {konversi}°C")
else:
    print("Unit suhu tidak valid. Harap masukkan 'C' atau 'F'.")
 