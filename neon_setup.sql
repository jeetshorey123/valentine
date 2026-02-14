-- ========================================
-- NEON POSTGRESQL DATABASE SETUP
-- Valentine App - Database Schema
-- ========================================

-- 🔴 IMPORTANT: YOU MUST RUN THIS SQL IN NEON CONSOLE! 🔴
-- 
-- STEPS TO RUN:
-- 1. Go to: https://console.neon.tech/
-- 2. Click on your project (ep-cool-pine-aifh81rb)
-- 3. Click "SQL Editor" in the left sidebar
-- 4. Copy this ENTIRE file content
-- 5. Paste into the SQL Editor
-- 6. Click "Run" button (or press Ctrl+Enter)
-- 
-- If you don't run this SQL, you will get error:
-- "relation 'valentines' does not exist"
-- ========================================

-- Step 1: Drop existing table if it exists
DROP TABLE IF EXISTS valentines CASCADE;

-- Step 2: Create the valentines table
CREATE TABLE valentines (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    response TEXT NOT NULL,
    review TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Step 3: Add indexes for better performance
CREATE INDEX idx_valentines_created_at ON valentines(created_at DESC);
CREATE INDEX idx_valentines_name ON valentines(name);

-- ========================================
-- ✅ DONE! Verify the table was created:
-- ========================================
-- Run this query to check:
SELECT * FROM valentines;
-- 
-- You should see: "0 rows" - that's correct!
-- Now your website can INSERT data into this table!
-- ========================================
