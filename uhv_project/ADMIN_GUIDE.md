# 🎛️ ADMIN DASHBOARD GUIDE

## 🔐 Access the Admin Panel

**URL:** `http://127.0.0.1:8000/admin/`

**Create Superuser:**
```bash
python manage.py createsuperuser
```

---

## 📊 ADMIN CAPABILITIES

### 1. **USER MANAGEMENT** 👥
**Location:** Admin → Users → Custom Users

**Features:**
- ✅ View all registered users
- ✅ Mark users as Students or Faculty
- ✅ Bulk actions: "Mark selected users as Students/Faculty"
- ✅ Search by username, email, name
- ✅ Filter by role, staff status, join date
- ✅ Edit user details and permissions

**Quick Actions:**
- Select multiple users → Actions → "Mark as Students"
- Select multiple users → Actions → "Mark as Faculty"

---

### 2. **REFLECTION SCENARIOS** 🤔
**Location:** Admin → Reflections → Reflection Scenarios

**Features:**
- ✅ Create new daily reflection scenarios
- ✅ Add 4 options inline (directly while creating scenario)
- ✅ Set active date for when scenario appears
- ✅ Categorize by value (Integrity, Trust, Respect, etc.)
- ✅ View total responses per scenario
- ✅ Edit explanation text for educational feedback

**How to Add:**
1. Click "Add Reflection Scenario"
2. Fill in title, scenario text, related value, date
3. Add 4 options in the inline form
4. Write educational explanation
5. Save

---

### 3. **USER RESPONSES** 📝
**Location:** Admin → Reflections → User Responses

**Features:**
- ✅ View all student responses
- ✅ Filter by value category and date
- ✅ Search by username or scenario
- ✅ See anonymous vs logged-in responses
- ✅ Track response patterns

**Read-only** - Cannot be edited (maintains data integrity)

---

### 4. **JOURNAL ENTRIES** 📔
**Location:** Admin → Journals → Journal Entries

**Features:**
- ✅ View all student journals
- ✅ See mood emojis (😊😌🤔🙏💪😕)
- ✅ View tags and word count
- ✅ Filter by mood and creation date
- ✅ Search by username or content
- ✅ Monitor student reflection quality

**Privacy Note:** Journals are private - only view for moderation/support

---

### 5. **ACTIVITIES** 🎯
**Location:** Admin → Activities → Activities

**Features:**
- ✅ Create new activities
- ✅ Upload activity images
- ✅ Set date, location, category
- ✅ Mark as upcoming/past (bulk actions)
- ✅ Filter by category and date
- ✅ See upcoming vs past activities

**Quick Actions:**
- Select activities → "Mark as past activities"
- Select activities → "Mark as upcoming activities"

---

### 6. **STUDENT VOICES** 💬
**Location:** Admin → Voices → Student Voices

**Features:**
- ✅ **Approve/Reject submissions**
- ✅ Bulk approve multiple voices
- ✅ View submission date
- ✅ See anonymous vs named submissions
- ✅ Moderate content before public display

**Approval Workflow:**
1. New voice submitted → `is_approved = False`
2. Admin reviews content
3. Select voice → Actions → "Approve selected voices"
4. Voice appears on public page

---

### 7. **FACULTY PROFILES** 👨‍🏫
**Location:** Admin → Faculty → Faculty Profiles

**Features:**
- ✅ Add faculty members
- ✅ Upload profile photos
- ✅ Set designation and bio
- ✅ Link to user accounts
- ✅ Manage faculty directory

---

### 8. **RESOURCES LIBRARY** 📚
**Location:** Admin → Resources → Resources

**Features:**
- ✅ Add articles, videos, PDFs, links
- ✅ Upload PDF files
- ✅ Add thumbnail images
- ✅ Mark as featured
- ✅ Categorize by value
- ✅ Track view counts
- ✅ Filter by type and category

**Resource Types:**
- Article (text content)
- Video (YouTube/external link)
- PDF (upload file)
- External Link

---

### 9. **INSPIRATIONAL QUOTES** 💭
**Location:** Admin → Quotes → Quotes

**Features:**
- ✅ Add new quotes
- ✅ Set author and category
- ✅ Enable/disable quotes
- ✅ Random quote appears on all pages
- ✅ Filter by category and status

---

### 10. **PROGRESS TRACKING** 📈
**Location:** Admin → Progress → User Progress

**Features:**
- ✅ **Visual streak charts** (last 30 days)
- ✅ View current streak with 🔥 indicators
- ✅ See longest streak 🏆
- ✅ Total reflections count
- ✅ Total journal entries
- ✅ Last reflection date
- ✅ Color-coded streak display:
  - Green 🔥 = 7+ days
  - Orange 🔥 = 3-6 days
  - Normal = 0-2 days

**Streak Visualization:**
- Green squares = Reflection completed
- Gray squares = No reflection
- Last 30 days displayed

---

### 11. **REFLECTION STREAKS** 🔥
**Location:** Admin → Progress → Reflection Streaks

**Features:**
- ✅ View daily completion status
- ✅ Mark days as completed/incomplete
- ✅ Bulk edit streaks
- ✅ Filter by completion status
- ✅ Date hierarchy for easy navigation

**Quick Actions:**
- Select days → "Mark as completed"
- Select days → "Mark as incomplete"

---

## 🎯 COMMON ADMIN TASKS

### **Daily Tasks:**
1. ✅ Approve new student voices
2. ✅ Check new journal entries (for support)
3. ✅ Monitor user activity

### **Weekly Tasks:**
1. ✅ Add new reflection scenarios (schedule for upcoming week)
2. ✅ Create new activities
3. ✅ Add new resources
4. ✅ Review student progress/streaks

### **Monthly Tasks:**
1. ✅ Add new quotes
2. ✅ Update faculty profiles
3. ✅ Generate reports (export data)
4. ✅ Review and archive old activities

---

## 🔍 SEARCH & FILTER

**Every admin page has:**
- 🔎 Search bar (top right)
- 🎛️ Filters (right sidebar)
- 📅 Date hierarchy (if applicable)
- 📊 List display with key info

---

## 💡 PRO TIPS

1. **Bulk Actions:** Select multiple items → Choose action from dropdown → Click "Go"
2. **Quick Edit:** Click on item name to edit
3. **Inline Editing:** Some fields can be edited directly in list view
4. **Export Data:** Use list filters → Select all → Export (if needed)
5. **Search:** Use search bar for quick access to specific items

---

## 🚀 QUICK START CHECKLIST

- [ ] Create superuser account
- [ ] Login to `/admin/`
- [ ] Add 5-7 reflection scenarios for the week
- [ ] Upload 3-5 resources
- [ ] Add 10+ inspirational quotes
- [ ] Create 2-3 upcoming activities
- [ ] Add faculty profiles
- [ ] Test approval workflow for student voices

---

## 📞 ADMIN DASHBOARD FEATURES

**Built-in Features:**
- ✅ Responsive design
- ✅ Search functionality
- ✅ Advanced filtering
- ✅ Bulk actions
- ✅ Inline editing
- ✅ Date hierarchies
- ✅ Custom actions
- ✅ Visual indicators
- ✅ Data validation
- ✅ Permission management

---

**Everything is ready to use! Access at:** `http://127.0.0.1:8000/admin/`
