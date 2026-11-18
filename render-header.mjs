import { animate } from 'animejs';
import { spawnSync } from 'node:child_process';

// Offline animation: GitHub receives a GIF, not executable JavaScript.
const cursor = { x: 0 };
const timeline = animate(cursor, { x: 1, duration: 1800, ease: 'inOutSine', autoplay: false });
const frames = Array.from({ length: 36 }, (_, i) => {
  timeline.seek(i <= 18 ? i * 100 : (36 - i) * 100);
  return cursor.x;
});
if (!(frames[9] > frames[0] && frames[18] > frames[9])) throw new Error('Animation did not advance');
const result = spawnSync('/usr/bin/python3', ['render-header.py'], { input: JSON.stringify(frames), encoding: 'utf8', stdio: ['pipe', 'inherit', 'inherit'] });
if (result.error || result.status !== 0) throw result.error || new Error(`Renderer exited ${result.status}`);
