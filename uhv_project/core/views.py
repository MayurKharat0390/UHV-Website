from django.shortcuts import render
from innovations.models import Innovation
from faculty.models import FacultyProfile
from .models import NewsUpdate, CoreValue
from .forms import ContactForm
from django.contrib import messages

def home(request):
    featured_innovations = Innovation.objects.filter(is_featured=True)[:3]
    faculties = FacultyProfile.objects.all()
    
    # Dynamic values from DB
    db_values = CoreValue.objects.all().prefetch_related('examples')
    values = []
    
    for v in db_values:
        example_dict = {ex.level: ex.text for ex in v.examples.all()}
        values.append({
            'name': v.name,
            'desc': v.description,
            'icon': v.icon,
            'examples': example_dict
        })

    # Fallback to hardcoded if DB is empty to prevent breakages during setup
    if not values:
        values = [
            {
                'name': 'Responsibility',
                'desc': 'Fulfilling one’s duty with care and dedication.',
                'icon': '🤝',
                'examples': {
                    'Family': 'Taking care of parents.',
                    'College': 'Submitting assignments on time.',
                    'Society': 'Following traffic rules.',
                    'Profession': 'Meeting project deadlines.'
                }
            },
            {
                'name': 'Trust',
                'desc': 'Assurance in the intention of the other.',
                'icon': '🌟',
                'examples': {
                    'Family': 'Believing in siblings.',
                    'College': 'Avoiding plagiarism.',
                    'Society': 'Honest transactions.',
                    'Profession': 'Keeping client data confidential.'
                }
            },
            {
                'name': 'Respect',
                'desc': 'Right evaluation of oneself and others.',
                'icon': '💚',
                'examples': {
                    'Family': 'Listening to elders.',
                    'College': 'Respecting teachers and peers.',
                    'Society': 'No discrimination.',
                    'Profession': 'Valuing colleagues’ time.'
                }
            },
            {
                'name': 'Harmony',
                'desc': 'Co-existence and mutual fulfillment.',
                'icon': '🎯',
                'examples': {
                    'Family': 'Spending quality time.',
                    'College': 'Group study and help.',
                    'Society': 'Community service.',
                    'Profession': 'Work-life balance.'
                }
            }
        ]


    return render(request, 'core/home.html', {
        'values': values,
        'featured_innovations': featured_innovations,
        'faculties': faculties,
    })

def uhv_cell(request):
    """
    View for the UHV Cell page with objectives and members.
    """
    # Objectives from the provided image
    objectives = [
        "Develop and implement programs such as SIP, UHV-I, UHV-II, and Minor Degree in UHV as per institute policy.",
        "Coordinate co-curricular programs like Faculty Mentor Program and Student Buddy Program.",
        "Guide extracurricular activities aligned with human values.",
        "Conduct training and orientation of faculty and staff in UHV and HVBE.",
        "Organize value-based outreach programs for the community.",
        "Regularly track, evaluate, and share progress with stakeholders."
    ]
    
    # Members from the provided image
    members = [
        {"sr": 1, "role": "Chairperson", "name": "Dr Govind N. Kulkarni", "dept": "Director, PCCOE", "image": "images/team/chairperson.png"},
        {"sr": 2, "role": "Convener", "name": "Dr. Mrs. K. Rajeswari", "dept": "Dean – Academics, PCCOE"},
        {"sr": 3, "role": "Coordinator", "name": "Ms Manjusha Devkule", "dept": "Institute UHV Coordinator"},
        {"sr": 4, "role": "Faculty Representative", "name": "Dr Mahesh Kolte", "dept": "Professor - E&TC, Dean Library and Learning Resource Development"},
        {"sr": "", "role": "Faculty Representative", "name": "Dr Sandeep Patil", "dept": "Asst. Professor - AS&H"},
        {"sr": "", "role": "Faculty Representative", "name": "Mrs. Rakhi Pagar", "dept": "Asst. Professor - IT"},
        {"sr": "", "role": "Faculty Representative", "name": "Dr Mrs. Shraddha Ovale", "dept": "Asst. Professor - Computer Engineering"},
        {"sr": "", "role": "Faculty Representative", "name": "Dr. Varsha Pandagare", "dept": "Asst. Professor - Computer Engineering (Reg.)"},
        {"sr": "", "role": "Faculty Representative", "name": "Dr. Jayesh Chordiya", "dept": "Asst. Professor - Mechanical Engineering"},
        {"sr": "", "role": "Faculty Representative", "name": "Ms. Vaishnavi Pujari", "dept": "Asst. Professor - Computer Science and Engineering (AIML)"},
        {"sr": "", "role": "Faculty Representative", "name": "Ms Pratima Kalokhe", "dept": "Asst. Professor - Civil Engineering"},
        {"sr": 5, "role": "Staff Representative", "name": "Mr. Sanjeev Upendra Aboti", "dept": "Registrar - Office"},
        {"sr": "", "role": "Staff Representative", "name": "Mr. Pratap Deokar", "dept": "Campus Incharge"},
        {"sr": "", "role": "Staff Representative", "name": "Mr. Ganesh Borade", "dept": "Support – Hostel Warden"},
    ]
    
    return render(request, 'core/uhv_cell.html', {
        'objectives': objectives,
        'members': members
    })

def contact(request):
    """
    View for the Contact Us page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for reaching out! Your message has been sent successfully. 🌟")
            return render(request, 'core/contact_success.html')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})
