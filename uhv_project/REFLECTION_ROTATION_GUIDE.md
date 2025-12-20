# 🔄 DAILY REFLECTION ROTATION SYSTEM

## ✅ **How It Works:**

The reflection system **automatically rotates** through all available scenarios, showing a **different one each day!**

---

## 📅 **Rotation Logic:**

### **Option 1: Scheduled Reflections (Priority)**
If you set a specific `active_date` for a scenario in the admin:
- That scenario will show **only on that date**
- Perfect for special occasions or themed weeks

### **Option 2: Automatic Rotation (Default)**
If no scenario is scheduled for today:
- System **automatically rotates** through ALL scenarios
- Uses **day of year** to calculate which one to show
- **Same scenario for everyone** on the same day
- **Different scenario tomorrow**

---

## 🎯 **Example:**

**You have 7 scenarios in the database:**

```
Day 1 (Jan 1): Scenario 1 - "Integrity in Action"
Day 2 (Jan 2): Scenario 2 - "Harmony at Home"
Day 3 (Jan 3): Scenario 3 - "Responsibility"
Day 4 (Jan 4): Scenario 4 - "Respect for Others"
Day 5 (Jan 5): Scenario 5 - "Truth in Communication"
Day 6 (Jan 6): Scenario 6 - "Trust Building"
Day 7 (Jan 7): Scenario 7 - "Compassion"
Day 8 (Jan 8): Scenario 1 - "Integrity in Action" (cycles back)
```

**Formula:** `Day of Year % Total Scenarios = Scenario Index`

---

## 💡 **Benefits:**

✅ **Always Fresh** - Different reflection every day  
✅ **Consistent** - Everyone sees same scenario on same day  
✅ **Automatic** - No manual scheduling needed  
✅ **Flexible** - Can override with specific dates  
✅ **Fair** - Cycles through all scenarios equally  

---

## 🎨 **How to Use:**

### **Method 1: Let It Auto-Rotate (Recommended)**
1. Add scenarios via admin (no specific date needed)
2. System automatically rotates daily
3. Students see different reflection each day
4. Cycles back to start after all scenarios shown

### **Method 2: Schedule Specific Dates**
1. Go to Admin → Reflections → Reflection Scenarios
2. Edit a scenario
3. Set `Active Date` to specific date
4. That scenario will show **only on that date**
5. Other days use auto-rotation

### **Method 3: Hybrid Approach**
- Schedule important dates (e.g., Republic Day, Gandhi Jayanti)
- Let other days auto-rotate
- Best of both worlds!

---

## 📊 **Current Setup:**

You currently have **7 scenarios** in the database:
1. Integrity in Action
2. Harmony at Home
3. Responsibility in Group Work
4. Respect for Diversity
5. Truth in Communication
6. Trust Building
7. Compassion in Action

**These will rotate automatically every day!**

---

## 🔧 **Admin Control:**

### **To Add More Scenarios:**
1. Admin → Reflections → Add Reflection Scenario
2. Fill in title, scenario text, value
3. Add 4 options
4. Leave `active_date` blank for auto-rotation
5. Save

### **To Schedule for Specific Date:**
1. Edit any scenario
2. Set `Active Date` to desired date
3. Save
4. That scenario will show on that date only

### **To See What's Showing Today:**
- Visit `/reflections/` as a student
- Or check admin console logs

---

## 📅 **Example Schedule:**

**Week 1:**
- Monday: Integrity
- Tuesday: Harmony
- Wednesday: Responsibility
- Thursday: Respect
- Friday: Truth
- Saturday: Trust
- Sunday: Compassion

**Week 2:**
- Monday: Integrity (cycles back)
- Tuesday: Harmony
- ... and so on

---

## 🎯 **Special Dates:**

You can schedule specific scenarios for:
- **Independence Day** - Patriotism scenario
- **Gandhi Jayanti** - Non-violence scenario
- **Exam Week** - Integrity in exams
- **Festival Days** - Harmony and respect
- **New Year** - Goal-setting reflection

---

## 💻 **Technical Details:**

**Calculation:**
```python
day_of_year = today.timetuple().tm_yday  # 1-365
scenario_count = 7  # total scenarios
scenario_index = day_of_year % scenario_count  # 0-6
```

**Example:**
- Jan 1 (day 1): 1 % 7 = 1 → Scenario #1
- Jan 2 (day 2): 2 % 7 = 2 → Scenario #2
- Jan 8 (day 8): 8 % 7 = 1 → Scenario #1 (cycles)

---

## ✨ **Best Practices:**

1. **Add 7+ Scenarios** - One for each day of week
2. **Diverse Topics** - Cover all 5 core values
3. **Update Regularly** - Add new scenarios monthly
4. **Schedule Special Days** - Use active_date for events
5. **Monitor Engagement** - Check response counts in admin

---

## 🚀 **Quick Start:**

**Current Status:**
- ✅ 7 scenarios already added
- ✅ Auto-rotation enabled
- ✅ Different reflection each day
- ✅ Ready to use!

**What Students See:**
- Today's unique reflection scenario
- 4 thoughtful options
- Different scenario tomorrow
- Consistent experience for all

---

**The system is fully automatic and ready!** 🎉

Students will see a **new reflection every day**, cycling through all scenarios fairly and automatically!
