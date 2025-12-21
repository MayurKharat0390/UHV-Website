# 🚂 Railway Deployment Guide for UHV Website

This guide will help you deploy your Universal Human Values (UHV) Django project to Railway.

## 📋 Prerequisites

1. A [Railway account](https://railway.app/) (sign up with GitHub)
2. Git installed on your computer
3. Your project pushed to a GitHub repository

## 🚀 Deployment Steps

### Step 1: Prepare Your Repository

Make sure all the new files are committed to your Git repository:

```bash
git add .
git commit -m "Add Railway deployment configuration"
git push origin main
```

### Step 2: Create a New Railway Project

1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your `UHV-Website` repository
5. Railway will automatically detect it's a Django project

### Step 3: Add PostgreSQL Database

1. In your Railway project dashboard, click **"+ New"**
2. Select **"Database"**
3. Choose **"PostgreSQL"**
4. Railway will automatically create a PostgreSQL database and set the `DATABASE_URL` environment variable

### Step 4: Configure Environment Variables

In your Railway project settings, add the following environment variables:

1. Click on your service (not the database)
2. Go to **"Variables"** tab
3. Add these variables:

```
SECRET_KEY=your-super-secret-key-here-generate-a-new-one
DEBUG=False
ALLOWED_HOSTS=.railway.app
```

**To generate a secure SECRET_KEY**, run this in your local terminal:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5: Deploy

1. Railway will automatically deploy your application
2. Wait for the build to complete (you can watch the logs)
3. Once deployed, Railway will provide you with a URL like: `https://your-app.up.railway.app`

### Step 6: Create Superuser (Admin Account)

After deployment, you need to create an admin account:

1. In Railway dashboard, go to your service
2. Click on **"Settings"** tab
3. Scroll down to **"Service"** section
4. Click **"Open Terminal"** or use Railway CLI
5. Run:
```bash
python manage.py createsuperuser
```
6. Follow the prompts to create your admin account

### Step 7: Load Initial Data (Optional)

If you want to populate your database with initial data:

```bash
python manage.py shell
```

Then run your seed scripts or manually add data through the admin panel.

## 🔧 Post-Deployment Configuration

### Access Your Site

- **Main Site**: `https://your-app.up.railway.app`
- **Admin Panel**: `https://your-app.up.railway.app/admin`

### Custom Domain (Optional)

1. In Railway project settings, go to **"Settings"** tab
2. Scroll to **"Domains"** section
3. Click **"Generate Domain"** for a custom Railway domain
4. Or add your own custom domain

## 📁 Files Created for Railway

- `Procfile` - Tells Railway how to run your app
- `runtime.txt` - Specifies Python version
- `railway.json` - Railway build and deploy configuration
- `requirements.txt` - Updated with production dependencies
- `.railwayignore` - Files to exclude from deployment
- `.env.example` - Example environment variables
- `settings.py` - Updated with production settings

## 🔍 Troubleshooting

### Build Fails

- Check the build logs in Railway dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify Python version in `runtime.txt`

### Static Files Not Loading

- Make sure `collectstatic` ran during build (check logs)
- Verify `STATIC_ROOT` is set correctly
- WhiteNoise should handle static files automatically

### Database Connection Issues

- Ensure PostgreSQL database is created in Railway
- Check that `DATABASE_URL` environment variable is set
- Verify `psycopg2-binary` is in requirements.txt

### 500 Internal Server Error

- Check application logs in Railway dashboard
- Verify all environment variables are set correctly
- Make sure `DEBUG=False` in production
- Check `ALLOWED_HOSTS` includes your Railway domain

## 🔄 Updating Your Deployment

To deploy updates:

```bash
git add .
git commit -m "Your update message"
git push origin main
```

Railway will automatically detect the changes and redeploy.

## 📊 Monitoring

- **Logs**: View real-time logs in Railway dashboard
- **Metrics**: Monitor CPU, memory, and network usage
- **Database**: Check PostgreSQL metrics and connection count

## 💰 Pricing

Railway offers:
- **Free Tier**: $5 of usage per month (enough for small projects)
- **Pro Plan**: $20/month with $20 of usage included

Your Django app should easily fit within the free tier for development/testing.

## 🛡️ Security Checklist

- ✅ `DEBUG=False` in production
- ✅ Strong `SECRET_KEY` generated
- ✅ HTTPS enabled (automatic on Railway)
- ✅ Secure cookies enabled
- ✅ HSTS headers configured
- ✅ PostgreSQL database with Railway's security

## 📞 Support

- [Railway Documentation](https://docs.railway.app/)
- [Railway Discord](https://discord.gg/railway)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)

---

**Your UHV Website is now ready for production! 🎉**
