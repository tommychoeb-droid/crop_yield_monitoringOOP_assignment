# OOP1 Assignment: Crop Yield Monitoring System

## 1. Project Overview

This project is a Python Object-Oriented Programming (OOP) application for monitoring crop yield records. It addresses a real-world agriculture use case by allowing users to add crop records, view stored records, search for a crop, and compare actual yield with expected yield.

The program is intentionally simple and modular so that it can be extended later without redesigning the entire system.

## 2. OOP Concepts Demonstrated

### Class 1: `Crop`
Represents an individual crop record.

Attributes:
- `crop_id`
- `farmer_name`
- `crop_type`
- `area_hectares`
- `expected_yield_kg`
- `actual_yield_kg`

Methods:
- `calculate_yield_difference()` - instance method
- `yield_status()` - instance method
- `display_info()` - instance method
- `create_from_input()` - class method using `@classmethod`

### Class 2: `CropYieldMonitor`
Manages multiple `Crop` objects.

Attributes:
- `crops` - a list containing Crop objects

Methods:
- `add_crop()`
- `search_crop()`
- `display_all()`
- `search_and_display()`

The two classes interact because `CropYieldMonitor` stores and operates on `Crop` objects.

## 3. Python Data Structure

Only one collection data structure is used: a **list**.

```python
self.crops = []
```

Multiple `Crop` objects are stored in this list. The program loops through the list when displaying records or searching for a crop.

## 4. Search Function

The `search_crop()` method searches the list using a crop ID.

```python
for crop in self.crops:
    if crop.crop_id.lower() == crop_id.lower():
        return crop
```

This makes the search case-insensitive.

## 5. Digital Public Goods (DPG) Alignment

### Open-source
The source code is written in Python and can be uploaded to GitHub for public access, reuse, inspection, and modification.

### Inclusive and accessible design
The application uses a simple text-based menu and clear prompts. It does not require expensive hardware, graphics, or advanced technical knowledge to operate.

### Privacy-respecting
The program does not request or store sensitive personal information such as national ID numbers, passwords, financial details, or medical records. The farmer name is used only as a simple crop-record label for the assignment demonstration.

### Modular and reusable
The program separates crop data (`Crop`) from record management (`CropYieldMonitor`). This makes the classes reusable and makes future features easier to add.

## 6. How to Run

1. Install Python 3.
2. Save `oop1_crop_yield_monitoring.py`.
3. Open a terminal in the project folder.
4. Run:

```bash
python oop1_crop_yield_monitoring.py
```

No external Python packages are required.

## 7. Example Usage

When the program starts, two sample objects are loaded:

- C001: Musa Kamara, Rice
- C002: Abdul Sesay, Cassava

Example actions:

```text
1. Add crop record
2. View all crop records
3. Search for a crop
4. Exit
```

Searching for `C001` displays the corresponding crop record and its yield status.

## 8. Files

- `oop1_crop_yield_monitoring.py` - Python source code
- `sample_output.txt` - example execution output
- `OOP1_Assignment_Report.docx` - written assignment documentation

