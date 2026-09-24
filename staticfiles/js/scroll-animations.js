/**
 * scroll-animations.js — High-Performance Scroll Reveal Engine
 * Uses modern IntersectionObserver for butter-smooth 60fps animations.
 */

(function () {
    'use strict';

    function initScrollAnimations() {
        // Elements to observe
        const revealElements = document.querySelectorAll(
            '.reveal, .reveal-left, .reveal-right, .reveal-zoom, .reveal-stagger, .reveal-fade-up'
        );

        if (!revealElements.length) return;

        // Check if IntersectionObserver is supported
        if (!('IntersectionObserver' in window)) {
            revealElements.forEach(el => el.classList.add('is-revealed'));
            return;
        }

        const observerOptions = {
            root: null,
            rootMargin: '0px 0px -40px 0px', // Trigger slightly before element enters full view
            threshold: 0.12
        };

        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-revealed');
                    obs.unobserve(entry.target); // Unobserve once revealed for optimal performance
                }
            });
        }, observerOptions);

        revealElements.forEach(el => {
            // If already above the fold, reveal immediately
            const rect = el.getBoundingClientRect();
            if (rect.top < window.innerHeight && rect.bottom > 0) {
                el.classList.add('is-revealed');
            } else {
                observer.observe(el);
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initScrollAnimations);
    } else {
        initScrollAnimations();
    }
})();
