-- Neon PostgreSQL Database Setup for Valentine App
-- Run this SQL in your Neon SQL Editor
-- Dashboard: https://console.neon.tech/

-- Drop existing table if it exists
DROP TABLE IF EXISTS valentines CASCADE;

-- Create the valentines table
CREATE TABLE valentines (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    response TEXT NOT NULL,
    review TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Add indexes for better performance
CREATE INDEX idx_valentines_created_at ON valentines(created_at DESC);
CREATE INDEX idx_valentines_name ON valentines(name);

-- ✅ DONE! Test by running this query:
-- SELECT * FROM valentines;

-- You should now be able to INSERT from your website!
