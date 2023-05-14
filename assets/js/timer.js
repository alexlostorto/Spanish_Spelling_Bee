class Timer {
    constructor(element) {
        this.element = element;
        this.active = false;
    }

    async start(duration) {
        this.active = true;
        this.element.textContent = duration;

        while (duration >= 0) {
            if (!this.active) return false;

            await sleep(1000);
            duration--;
            this.element.textContent = duration;
        }

        return true;
    }

    stop() {
        this.active = false;
    }
}