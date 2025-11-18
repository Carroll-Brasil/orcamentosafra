import { useState, useEffect } from 'react';

export function useMediaQuery(query: string): boolean {
  const [matches, setMatches] = useState<boolean>(false); // Default to false ensuring server and client match

  useEffect(() => {
    // Effect runs only on the client
    const matchMedia = window.matchMedia(query);

    // Set the state to the correct value on the client
    setMatches(matchMedia.matches);

    // Create a listener for changes
    const handleChange = () => {
      setMatches(matchMedia.matches);
    };

    // Add the listener
    // Using addEventListener is the modern and recommended way
    matchMedia.addEventListener('change', handleChange);

    // Cleanup function to remove the listener
    return () => {
      matchMedia.removeEventListener('change', handleChange);
    };
  }, [query]); // Re-run effect if query changes

  return matches;
}
