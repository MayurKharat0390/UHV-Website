import os
import django
import shutil

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uhv_project.settings')
django.setup()

from voices.models import StudentVoice, StoryMedia

def add_pavan_voice():
    # 1. Image path
    src_img = r"C:\Users\MAYUR KHARAT\.gemini\antigravity\brain\7e8f0400-6bcb-4eb7-a2b0-4397ccfd0a2e\media__1773417710509.png"
    dest_dir = "media/story_media"
    os.makedirs(dest_dir, exist_ok=True)
    
    img_name = "pavan_chavan.png"
    dest_path = os.path.join(dest_dir, img_name)
    
    if os.path.exists(src_img):
        shutil.copy(src_img, dest_path)
        print(f"Copied image to {dest_path}")
    else:
        print(f"Source image NOT found: {src_img}")
        return

    # 2. Testimonial Text
    name = "Chavan Pavan Devkrushna (Mechanical - Third Year)"
    content = (
        "Choosing UHV as my MDM subject at PCCOE was a life-changing decision. Beyond academics, UHV shaped my mindset "
        "for the professional world. During an internship interview for a 6 LPA PPO, the recruiters emphasized that "
        "values matter more than technical skill. By applying UHV principles—honesty, humility, and transparency—I stood "
        "out among candidates and secured the selection. UHV is more than a subject; it's a guide for building "
        "self-awareness and integrity."
    )

    # 3. Create Voice Entry
    voice, created = StudentVoice.objects.get_or_create(
        name_display=name,
        defaults={
            'content': content,
            'is_approved': True
        }
    )
    
    if created:
        # 4. Attach Media
        StoryMedia.objects.create(
            story=voice,
            file=f"story_media/{img_name}"
        )
        print(f"Successfully added impact story for {name}")
    else:
        print(f"Impact story for {name} already exists.")

if __name__ == "__main__":
    add_pavan_voice()
