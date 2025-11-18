import type { NextConfig } from "next";

// Pin the tracing root to this project to avoid Next.js
// walking up to C:\\Users\\miguel due to other lockfiles (e.g., bun.lock),
// which caused it to read a BOM-prefixed package.json and crash.
const nextConfig: NextConfig = {
  outputFileTracingRoot: process.cwd(),
};

export default nextConfig;
