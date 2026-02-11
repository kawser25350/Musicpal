# Musicpal - Django Music Management System

A Django web application for managing musicians and their albums without authentication. This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using Django models and forms.

##  Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Models Explained](#models-explained)
- [Forms Explained](#forms-explained)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)

##  Overview

Musicpal is a simple Django application that allows you to manage musicians and their music albums. The project consists of two main apps:
- **musician**: Manages musician information
- **album**: Manages music albums linked to musicians

##  Features

- ✅ Add, edit, and delete musicians
- ✅ Add, edit, and delete albums
- ✅ Link albums to specific musicians (Foreign Key relationship)
- ✅ Form validation for data integrity
- ✅ No authentication required (open access)
- ✅ SQLite database for data persistence

##  Project Structure

```
Musicpal/
├── musician/           # Musician app
│   ├── models.py      # Musician model
│   ├── forms.py       # Musician form with validation
│   ├── views.py       # CRUD views for musicians
│   ├── urls.py        # URL routing
│   └── Templates/     # HTML templates
├── album/             # Album app
│   ├── models.py      # Album model
│   ├── forms.py       # Album form
│   ├── views.py       # CRUD views for albums
│   ├── urls.py        # URL routing
│   └── Templates/     # HTML templates
├── project2/          # Main project settings
│   ├── settings.py    # Django settings
│   ├── urls.py        # Main URL configuration
│   └── views.py       # Home page view
├── Templates/         # Global templates
├── db.sqlite3         # SQLite database
└── manage.py          # Django management script
```

---

##  Models Explained

### 1. Musician Model

**Location**: `musician/models.py`

```python
class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=11)
    instrument_type = models.CharField()

    def __str__(self):
        return f"{self.first_name}"
```

**Fields:**
- **`first_name`**: CharField with max length of 100 characters - stores musician's first name
- **`last_name`**: CharField with max length of 100 characters - stores musician's last name
- **`email`**: EmailField - automatically validates email format
- **`number`**: CharField with max length of 11 characters - stores contact number (stored as text to preserve leading zeros)
- **`instrument_type`**: CharField - stores the type of instrument the musician plays

**Methods:**
- **`__str__()`**: Returns the musician's first name when the object is converted to string (useful in admin panel and dropdowns)

**Note**: There's a small issue in line 9 - `instrument_type` is missing a `max_length` parameter, which should be added for proper database schema definition.

---

### 2. Album Model

**Location**: `album/models.py`

```python
class Album(models.Model):
    album_name = models.CharField(max_length=200)
    album_release_date = models.DateTimeField()
    r_choices = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = models.IntegerField(choices=r_choices)
    author = models.ForeignKey(Musician, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.album_name}"
```

**Fields:**
- **`album_name`**: CharField with max length of 200 characters - stores the album title
- **`album_release_date`**: DateTimeField - stores the date and time when the album was released
- **`rating`**: IntegerField with choices - allows rating from 1 to 5 stars
  - Uses `r_choices` list to restrict values to 1-5
  - First value in tuple is stored in database, second is displayed to users
- **`author`**: ForeignKey to Musician model
  - Creates a many-to-one relationship (many albums can belong to one musician)
  - `on_delete=models.CASCADE` means if a musician is deleted, all their albums are automatically deleted

**Methods:**
- **`__str__()`**: Returns the album name when the object is converted to string

**Relationship:**
```
Musician (1) ----< (Many) Album
```
One musician can have multiple albums, but each album belongs to only one musician.

---

##  Forms Explained

### 1. MusicianForm

**Location**: `musician/forms.py`

```python
class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'number': 'Contact',
            'instrument': 'Instrument'
        }
        
        help_texts = {
            'first_name': 'Enter Your First Name',
            'last_name': 'Enter Your Last Name',
            'email': 'Enter Your Email',
            'number': 'Enter Your Contact',
            'instrument': 'Enter Your Instrument Name'
        }
```

**Features:**
- **ModelForm**: Automatically creates form fields based on the Musician model
- **`fields = '__all__'`**: Includes all model fields in the form
- **`labels`**: Customizes the display labels for each field (user-friendly names)
- **`help_texts`**: Provides helpful hints below each form field

**Custom Validation** (lines 25-39):
The form includes a `clean()` method for custom validation:
- ✅ **Name validation**: Ensures first and last names are not numbers
- ✅ **Phone validation**: Ensures contact number is exactly 11 digits
- ✅ **Email validation**: Ensures email contains '@gmail.com'

**Example validation:**
```python
def clean(self):
    clean_data = super().clean()
    first_name = clean_data.get('first_name')
    
    if first_name and first_name.isdigit():
        raise forms.ValidationError('User name cannot be number')
    
    return clean_data
```

---

### 2. AlbumForm

**Location**: `album/forms.py`

```python
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        
        labels = {
            'album_name': 'Album Name',
            'album_release_date': 'Release Date',
            'rating': 'Rating',
            'author': 'Author'
        }
        
        help_texts = {
            'album_name': 'Enter Album Name',
            'album_release_date': 'Enter Release Date',
            'rating': 'Enter Rating',
            'author': 'Enter Author'
        }
        
        widgets = {
            'album_release_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
```

**Features:**
- **ModelForm**: Automatically creates form fields based on the Album model
- **`fields = '__all__'`**: Includes all model fields in the form
- **`labels`**: Custom display labels for better UX
- **`help_texts`**: Guidance text for each field
- **`widgets`**: Customizes how fields are rendered
  - **`datetime-local`**: Uses HTML5 datetime picker for the release date field, providing a user-friendly calendar interface

**Form Fields Generated:**
1. **album_name**: Text input
2. **album_release_date**: DateTime picker (with custom widget)
3. **rating**: Dropdown select with options 1-5
4. **author**: Dropdown select populated with all musicians from database

---

##  Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/kawser25350/Musicpal.git
   cd Musicpal
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Django**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Home: http://127.0.0.1:8000/
   - Musicians: http://127.0.0.1:8000/musician/
   - Albums: http://127.0.0.1:8000/album/
   - Admin: http://127.0.0.1:8000/admin/

---

##  Usage

### Managing Musicians

**Add Musician:**
1. Navigate to `/musician/add/`
2. Fill in the form:
   - First Name
   - Last Name
   - Email (must contain @gmail.com)
   - Contact Number (must be 11 digits)
   - Instrument Type
3. Submit the form

**View Musicians:**
- Navigate to `/musician/` to see all musicians

**Edit Musician:**
- Click edit button on musician list
- Update the information
- Submit changes

**Delete Musician:**
- Click delete button on musician list
- ⚠️ Warning: This will also delete all albums by this musician (CASCADE delete)

### Managing Albums

**Add Album:**
1. Navigate to `/album/add/`
2. Fill in the form:
   - Album Name
   - Release Date (use datetime picker)
   - Rating (1-5 stars)
   - Author (select from existing musicians)
3. Submit the form

**View Albums:**
- Navigate to `/album/` to see all albums

**Edit Album:**
- Click edit button on album list
- Update the information
- Submit changes

**Delete Album:**
- Click delete button on album list

---

##  Key Django Concepts Demonstrated

### 1. **Models (Database Layer)**
- Model field types (CharField, EmailField, DateTimeField, IntegerField)
- ForeignKey relationships (one-to-many)
- CASCADE deletion behavior
- `__str__()` method for object representation

### 2. **Forms (User Input Layer)**
- ModelForm for automatic form generation
- Custom labels and help texts
- Custom validation with `clean()` method
- Custom widgets for better UX
- Field choices for restricted options

### 3. **Views (Business Logic Layer)**
- Function-based views
- GET vs POST request handling
- CRUD operations using Django ORM:
  - **Create**: `form.save()`
  - **Read**: `Model.objects.all()`, `Model.objects.get(pk=id)`
  - **Update**: `form.save()` with `instance` parameter
  - **Delete**: `object.delete()`
- Redirects after successful operations

### 4. **Database Operations**
```python
# Create
form.save()

# Read All
Album.objects.all()

# Read One
Album.objects.get(pk=id)

# Update
form = AlbumForm(request.POST, instance=existing_album)
form.save()

# Delete
album.delete()
```

---

##  Learning Outcomes

By studying this project, you'll understand:
- ✅ How to create Django models with relationships
- ✅ How to use ModelForms for rapid form development
- ✅ How to implement CRUD operations without authentication
- ✅ How to validate user input in Django forms
- ✅ How ForeignKey relationships work (CASCADE deletion)
- ✅ How to customize form fields with labels, help texts, and widgets
- ✅ Basic Django project structure and organization

---

##  Known Issues

1. **musician/models.py line 9**: `instrument_type` field is missing `max_length` parameter
   ```python
   # Current (will cause warnings)
   instrument_type = models.CharField()
   
   # Should be
   instrument_type = models.CharField(max_length=100)
   ```

2. **No authentication**: Application is open to all users without login requirements

---

##  Contributing

Feel free to fork this project and submit pull requests for improvements!

---

##  License

This project is open source and available for educational purposes.

---

##  Author

**kawser25350**
- GitHub: [@kawser25350](https://github.com/kawser25350)

---

##  Acknowledgments

This project serves as a beginner-friendly example of Django's core features for database interaction without the complexity of authentication systems.
