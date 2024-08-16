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
    document.documentElement.setAttribute('data-theme', theme);
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
            }}><ConstrastIcon /></ConfigButton>
        </div>
    );
}