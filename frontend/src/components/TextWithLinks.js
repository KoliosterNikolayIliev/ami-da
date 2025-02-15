import React from 'react';

const TextWithLinks = ({ text }) => {
    // Regular expression to match URLs
    const urlRegex = /(https?:\/\/[^\s]+)/g;

    // Split text into parts, replacing URLs with anchor tags
    const formattedText = text.split(urlRegex).map((part, index) => {
        if (urlRegex.test(part)) {
            // If the part is a URL, render it as a link
            return (
                <a key={index} href={part} target="_blank" rel="noopener noreferrer">
                    {part}
                </a>
            );
        }
        // Otherwise, render it as plain text
        return part;
    });

    return <p>{formattedText}</p>;
};

export default TextWithLinks;