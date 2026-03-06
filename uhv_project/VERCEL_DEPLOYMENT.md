# Hosting Django on Vercel

This guide explains how to deploy this Django application to Vercel.

## 1. Prerequisites

- A [Vercel](https://vercel.com) account.
- The `vercel` CLI installed globally (optional but recommended for local testing): `npm i -g vercel`.
- A PostgreSQL database (e.g., Supabase, Neon, or Railway) or another database hosted somewhere, as Vercel uses serverless functions, meaning SQLite will lose its data every time the function spins down.

## 2. Configuration Files

The following configuration files have already been added to the project for Vercel support:
- `vercel.json`: Tells Vercel how to build the app, defining the Python runtime and mapping the routes.
- `build_files.sh`: A simple script that Vercel executes to install `requirements.txt` and collect static files.
- `uhv_project/wsgi.py`: Modified to include `app = application` because Vercel looks for an `app` variable for WSGI applications.
- `uhv_project/settings.py`: Updated `ALLOWED_HOSTS` to allow `.vercel.app`.

## 3. Database Consideration (IMPORTANT)

Vercel functions are stateless and read-only (except for `/tmp`). The default `db.sqlite3` will not persist data in production! 

**You must use an external database like PostgreSQL.**

In Vercel's environment settings, add:
- `DATABASE_URL` (Your remote PostgreSQL connection string)
- `SECRET_KEY` (A secure random string)
- `DEBUG` = `False`

## 4. Deployment Steps

There are two primary ways to deploy to Vercel:

### Option A: Deploy via GitHub (Recommended)
1. Push your code to a GitHub repository.
2. Go to your Vercel Dashboard and click **Add New** -> **Project**.
3. Import your GitHub repository.
4. Expand the **Environment Variables** section and add `SECRET_KEY` and `DATABASE_URL`.
5. Click **Deploy**. Vercel will automatically detect the `vercel.json` and build the app.

### Option B: Deploy via Vercel CLI
1. Open up your terminal in this directory.
2. Run `vercel`.
3. Follow the prompts to link your project.
4. Add environment variables using the CLI: `vercel env add SECRET_KEY` and `vercel env add DATABASE_URL`.
5. Run `vercel --prod` to push to production.

## Troubleshooting

- **Static Files Not Loading**: Ensure `collectstatic` runs fully in `build_files.sh` and the generated files are within `staticfiles/`. Our `vercel.json` routes `/static/(.*)` to the correctly built static files folder.
- **Server Error (500)**: Often caused by missing environment variables (`SECRET_KEY`, `DATABASE_URL`). Check the "Logs" tab inside your Vercel project dashboard.
- **Database Locked/Read Only**: You are likely trying to use the SQLite file. Switch to an external PostgreSQL database since Vercel's file system is essentially read-only during runtime.
