'use client';
import React, { ReactNode, MouseEventHandler, useState, useEffect } from 'react';
import styles from '@/styles/components/ConfigButton.module.css';

interface ConfigButtonProps {
    children: ReactNode;
    onClick?: MouseEventHandler<HTMLButtonElement>;
    position?: 'topleft' | 'topright' | 'bottomleft' | 'bottomright';
    variant?: 'default' | 'outline' | 'borderless';
    disabled?: boolean;
    redirectURL?: string | null;
}

const ConfigButton: React.FC<ConfigButtonProps> = ({ children, onClick, position = 'bottomleft', variant = 'default', disabled, redirectURL = null }) => {
    var fvariant = `rounded-lg bg-white shadow-lg bg-base-100 bg-opacity-15 backdrop-blur-md`;
    if (variant === 'outline') {
        fvariant = `rounded-lg border-2 border-blue-500 text-blue-600`;
    } else if (variant === 'borderless') {
        fvariant = `rounded-lg`;
    }

    const handleClick = () => {
        // @ts-ignore
        window.location.href = redirectURL;
    }

    return (
        <button
            className={`${fvariant} ${styles.configbutton} ${styles[position]}`}
            onClick={redirectURL === null ? onClick : handleClick}
            disabled={disabled}
        >
            {children}
        </button>
    )
}

export default ConfigButton;