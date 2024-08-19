'use client';
import { useEffect } from 'react';
import ConstrastIcon from "@mui/icons-material/Contrast";
import ConfigButton from "@/components/ConfigButton";

const getPreferredColorScheme = (): string => {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        return 'dark';
    } else {
        return 'light';
    }
}

const setTheme = (theme: string) => {
    document.documentElement.setAttribute('data-theme', theme === 'dark' ? 'sunset' : 'light'); // maybe 'business' theme
    if (theme === "dark") {
        document.documentElement.classList.add("dark");
    } else {
        document.documentElement.classList.remove("dark");
    }
    localStorage.setItem("darkmode", theme);
}

export default function DarkModeWrapper({ children }: { children: React.ReactNode }) {
    useEffect(() => {
        const storedTheme = localStorage.getItem("darkmode") || getPreferredColorScheme();
        setTheme(storedTheme);
    }, []);

    return (
        <div>
            {children}
            <ConfigButton position="bottomright" onClick={(event) => {
                const currentTheme = localStorage.getItem("darkmode") === "dark" ? "light" : "dark";
                setTheme(currentTheme);
                // Ensure the button loses focus after click
                (event.target as HTMLElement).blur();
            }}>
                {/* <ConstrastIcon /> */}
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="size-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
                </svg>
            </ConfigButton>
        </div>
    );
}