-- ⚠️ CRITICAL FIX FOR SUPABASE RLS POLICY ERROR ⚠️
-- Run this ENTIRE code in Supabase SQL Editor
-- Link: https://supabase.com/dashboard/project/cjkbjehzblbgyehndkmy/sql/new

-- Step 1: Drop existing table and start fresh
DROP TABLE IF EXISTS valentines CASCADE;

-- Step 2: Create the valentines table
CREATE TABLE valentines (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    response TEXT NOT NULL,
    review TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Step 3: Add indexes for better performance
CREATE INDEX idx_valentines_created_at ON valentines(created_at DESC);
CREATE INDEX idx_valentines_name ON valentines(name);

-- Step 4: Enable Row Level Security
ALTER TABLE valentines ENABLE ROW LEVEL SECURITY;

-- Step 5: Create policies - THIS IS THE FIX!
-- Allow anonymous users (anon role) to INSERT
CREATE POLICY "anon_insert_policy"
ON valentines
FOR INSERT
TO anon
WITH CHECK (true);

-- Allow anonymous users (anon role) to SELECT
CREATE POLICY "anon_select_policy"
ON valentines
FOR SELECT
TO anon
USING (true);

-- Allow anonymous users (anon role) to UPDATE
CREATE POLICY "anon_update_policy"
ON valentines
FOR UPDATE
TO anon
USING (true)
WITH CHECK (true);

-- Allow authenticated users to do everything (optional)
CREATE POLICY "authenticated_all_policy"
ON valentines
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

-- Step 6: Grant permissions to anon role
GRANT USAGE ON SCHEMA public TO anon;
GRANT ALL ON valentines TO anon;
GRANT USAGE, SELECT ON SEQUENCE valentines_id_seq TO anon;

-- ✅ DONE! Test by running this query:
-- SELECT * FROM valentines;

-- You should now be able to INSERT from your website!
