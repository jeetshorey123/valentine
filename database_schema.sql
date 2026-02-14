-- Valentine's Day Website Database Schema
-- Run this SQL in your Supabase SQL Editor

-- Create the valentines table
CREATE TABLE IF NOT EXISTS valentines (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    response TEXT NOT NULL,
    review TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Add indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_valentines_created_at ON valentines(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_valentines_name ON valentines(name);

-- Enable Row Level Security (RLS)
ALTER TABLE valentines ENABLE ROW LEVEL SECURITY;

-- ⚠️ CRITICAL: Policies must explicitly target 'anon' role
CREATE POLICY "anon_insert_policy"
ON valentines
FOR INSERT
TO anon
WITH CHECK (true);

CREATE POLICY "anon_select_policy"
ON valentines
FOR SELECT
TO anon
USING (true);

-- Allow authenticated users full access
CREATE POLICY "authenticated_all_policy"
ON valentines
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

-- Grant necessary permissions to anon role
GRANT USAGE ON SCHEMA public TO anon;
GRANT ALL ON valentines TO anon;
GRANT USAGE, SELECT ON SEQUENCE valentines_id_seq TO anon;

-- View all entries (for testing)
-- SELECT * FROM valentines ORDER BY created_at DESC;

-- Count total responses
-- SELECT COUNT(*) as total_responses FROM valentines;

-- Get responses by date
-- SELECT DATE(created_at) as date, COUNT(*) as count 
-- FROM valentines 
-- GROUP BY DATE(created_at) 
-- ORDER BY date DESC;
