# Tiny-Classifier Task-Routed Local Cascade

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-classifier-task-routed-local-cascade-c34568e5a265`
Run ID: `tiny-classifier-task-routed-local-cascade-c34568e5a265-20260619T034812208331+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/886dd2a97b95

## What looked useful

Reliable task routing is the gating condition. Across 18 controlled rows, the confidence cascade averaged +4.2 percentage points accuracy over dense with 0.626 expected active parameter ratio, but 1.60x measured latency. In high-router rows, cascade accuracy was +6.2 points with 0.175 expected active parameter ratio, still 1.58x dense latency.

## Boundaries and scale limits

Synthetic 32-dimensional inputs, four tasks, small MLP router/specialists/dense baseline, three random seeds, short local GPU runs. No real text/image tasks, no LLM-scale local models, no production batching/cache benchmark, and no total-parameter-matched dense baseline.

## Claim scope

On a synthetic 4-task PyTorch classification benchmark, a tiny router plus local specialists improves accuracy over a task-unaware dense baseline when task identity is recoverable from the input distribution, and can reduce expected active parameter count. The tested implementation does not improve measured latency.

## Why it stopped

No-paper useful signal: the synthetic mechanism is supported only under high routing separability, while the simple cascade fails the latency-saving claim in measured local inference.

## Recommended next action

Run a bounded real-task follow-up using frozen embeddings or small local models, a parameter-matched dense baseline, and a batched serving harness to test whether active-parameter savings translate into wall-clock savings.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-task batched routing test for tiny classifier cascades
- Success threshold: On held-out real-task data, cascade accuracy is no worse than 1 percentage point below the best dense baseline, exceeds dense by at least 3 points in one task family, and reduces measured p50 batch latency or tokens/examples per second cost by at least 20%.
- Stop condition: Stop if router task accuracy remains below 0.85 after calibration, or if batched cascade latency is not at least 10% better than dense in two independent task families.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-classifier-task-routed-local-cascade-c34568e5a265`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
