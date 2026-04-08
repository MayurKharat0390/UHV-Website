from django.shortcuts import render
from innovations.models import Innovation
from faculty.models import FacultyProfile
from .models import NewsUpdate, CoreValue
from .forms import ContactForm
from django.contrib import messages

def home(request):
    try:
        featured_innovations = Innovation.objects.filter(is_featured=True)[:3]
        faculties = FacultyProfile.objects.all()
        # Trigger query execution to catch table errors early
        list(featured_innovations)
        list(faculties)
        
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
    except Exception:
        featured_innovations = []
        faculties = []
        values = []

    # Hardcoded fallback values for Universal Human Values (4 Levels of Living)
    if not values:
        values = [
            {'name': 'Harmony in Self', 'desc': 'Realizing the co-existence of the Self (I) and the Body, ensuring right understanding and feelings.', 'icon': '🧘', 'theme': 'primary',
             'examples': {'Knowing': 'Self-exploration.', 'Doing': 'Right behavior.', 'Being': 'Happiness.', 'Living': 'Health.'}},
            {'name': 'Harmony in Family', 'desc': 'The basic unit of human interaction, where values like trust and respect are nurtured through right relationship.', 'icon': '🏡', 'theme': 'accent',
             'examples': {'Trust': 'Foundational value.', 'Respect': 'Right evaluation.', 'Affection': 'Kinship.', 'Gratitude': 'Honoring efforts.'}},
            {'name': 'Harmony in Society', 'desc': 'Extending relationship from family to the entire society, aiming for an undivided human race.', 'icon': '🤝', 'theme': 'violet',
             'examples': {'Trust': 'Fearlessness.', 'Prosperity': 'Right production.', 'Co-existence': 'Universal system.', 'Work': 'Service.'}},
            {'name': 'Harmony in Nature', 'desc': 'Living in harmony and co-existence with the animal, plant, and material worlds.', 'icon': '🌱', 'theme': 'emerald',
             'examples': {'Restraint': 'Cyclic usage.', 'Nurture': 'Protection.', 'Balance': 'Ecological health.', 'Unity': 'Inseparable link.'}}
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
        {"sr": 2, "role": "Convener", "name": "Dr. Mrs. K. Rajeswari", "dept": "Dean – Academics, PCCOE", "image": "images/team/k_rajeswari.jpg"},
        {"sr": 3, "role": "Coordinator", "name": "Ms Manjusha Devkule", "dept": "Institute UHV Coordinator", "image": "images/team/manjusha_devkule.png"},
        {"sr": 4, "role": "Faculty Representative", "name": "Dr Mahesh Kolte", "dept": "Professor - E&TC, Dean Library and Learning Resource Development", "image": "images/team/mahesh_kolte.png"},
        {"sr": "", "role": "Faculty Representative", "name": "Dr Sandeep Patil", "dept": "Asst. Professor - AS&H", "image": "images/team/sandeep_patil.png"},
        {"sr": "", "role": "Faculty Representative", "name": "Mrs. Rakhi Pagar", "dept": "Asst. Professor - IT", "image": "images/team/rakhi_pagar.png"},
        {"sr": "", "role": "Faculty Representative", "name": "Dr Mrs. Shraddha Ovale", "dept": "Asst. Professor - Computer Engineering", "image": "images/team/shraddha_ovale.png"},
        {"sr": "", "role": "Faculty Representative", "name": "Dr. Varsha Pandagare", "dept": "Asst. Professor - Computer Engineering (Reg.)", "image": "images/team/varsha_pandagare.png"},
        {"sr": "", "role": "Faculty Representative", "name": "Dr. Jayesh Chordiya", "dept": "Asst. Professor - Mechanical Engineering", "image": "images/team/jayesh_chordiya.png"},
        {"sr": "", "role": "Faculty Representative", "name": "Ms. Vaishnavi Pujari", "dept": "Asst. Professor - Computer Science and Engineering (AIML)", "image": "images/team/vaishnavi_pujari.png"},
        {"sr": "", "role": "Faculty Representative", "name": "Ms Pratima Kalokhe", "dept": "Asst. Professor - Civil Engineering", "image": "images/team/pratima_kalokhe.png"},
        {"sr": 5, "role": "Staff Representative", "name": "Mr. Sanjeev Upendra Aboti", "dept": "Registrar - Office", "image": "images/team/sanjeev_aboti.png"},
        {"sr": "", "role": "Staff Representative", "name": "Mr. Ganesh Borade", "dept": "Campus Incharge"},
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
