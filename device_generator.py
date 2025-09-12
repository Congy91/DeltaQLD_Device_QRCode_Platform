import pandas as pd

# Initialize lists
ids = []
device_names = []
device_numbers = []
device_types = []
device_serials = []
device_ips = []

# Base values
base_device_number = 10100
base_serial = 65624653
base_ip = 21  # Last octet starts at 21

for i in range(50):
    ids.append(i + 1)
    device_names.append(f"MSSB-1-{i+1}")
    device_numbers.append(base_device_number + i*100)
    device_types.append("Red5-PLUS-ROOM")
    device_serials.append(base_serial + i*100000)  # increment serial logically
    device_ips.append(f"192.168.10.{base_ip + i}")

# Create DataFrame
df = pd.DataFrame({
    "id": ids,
    "device_name": device_names,
    "device_number": device_numbers,
    "device_type": device_types,
    "device_serial": device_serials,
    "device_ip": device_ips
})

# Save to Excel
df.to_excel("devices_50.xlsx", index=False)
print("Excel file 'devices_50.xlsx' created successfully!")
