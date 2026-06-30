# Evidence-Led Agent Loop for Small Tool-Use Models on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-led-agent-loop-for-small-tool-use-models-on-cpu-d38f88b02d09`
Run ID: `evidence-led-agent-loop-for-small-tool-use-models-on-cpu-d38f88b02d09-20260608T061100951251+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c21b4dafbe61

## What looked useful

Across 9 noise cells and 270,000 task evaluations per agent, evidence-led accuracy exceeded baseline accuracy in every cell, with absolute accuracy gains from 0.2330 to 0.5159 and mean gain 0.4145. A retry-budget ablation at the central noise cell showed no gain at max_iters=1 and monotonic gains through max_iters=4, supporting the verification-backed retry mechanism.

## Boundaries and scale limits

No actual LLM inference or training was run. Tasks were synthetic arithmetic, lookup, and string transforms. Verifiers were task-specific and deterministic. Results do not establish broad real-world agent reliability, prompt robustness, or small-model latency/accuracy tradeoffs.

## Claim scope

In a controlled synthetic CPU benchmark with deterministic tools, task-specific verifiers, and a seeded noisy policy proxy for a weak tool-use model, evidence capture plus verification-backed retries improved exact-match task accuracy over a one-shot baseline across all tested noise settings.

## Why it stopped

Stopped with a no-paper useful signal because the current evidence is synthetic/proxy evidence rather than direct evaluation of an actual small tool-use model.

## Recommended next action

Run a bounded real-model follow-up using one CPU-capable small tool-use model, fixed prompts, the same one-shot versus evidence-led loop comparison, and held-out tool tasks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-Model Evidence-Led Tool Loop on CPU
- Success threshold: Evidence-led loop improves exact-match accuracy by at least 10 absolute percentage points over baseline with Wilson 95% intervals that do not overlap materially, while mean tool calls remain at or below 3x baseline.
- Stop condition: Stop if the real-model evidence-led loop fails to improve exact-match accuracy by 5 absolute percentage points on a 200-task smoke set or if CPU latency makes the bounded comparison exceed the local run budget.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-led-agent-loop-for-small-tool-use-models-on-cpu-d38f88b02d09`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
