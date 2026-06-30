# Sparse Top-K Gradient Delta Encoding for Simulated Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-top-k-gradient-delta-encoding-for-simulated-volunteer-training-4800197d0305`
Run ID: `sparse-top-k-gradient-delta-encoding-for-simulated-volunteer-training-4800197d0305-20260526T103651015179+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1a4d425f5a56

## What looked useful

Top-k delta without residual feedback reached 0.8542 mean accuracy at 5% k versus 0.8576 dense with 10.3x fewer bytes, and 0.8430 at 2% k with 25.6x fewer bytes. Naive top-k delta plus error feedback diverged badly, while top-k gradient plus error feedback was also competitive.

## Boundaries and scale limits

Synthetic logistic regression only; no real neural network, no real volunteer network, no asynchronous straggler model, no privacy/security overhead, no production serialization benchmark, and only three random seeds.

## Claim scope

In a deterministic synthetic non-IID logistic-regression volunteer-training simulator with 40 clients, 2048 parameters, 35% participation, and 200 rounds, top-k gradient delta encoding without residual feedback preserved most dense accuracy at 2-5% transmitted coordinates while reducing communicated bytes by about 10-26x.

## Why it stopped

Closed as no-paper useful signal: local synthetic evidence supports the delta-only mechanism but is insufficient for a publication-grade volunteer-training claim, and naive delta error feedback was unstable.

## Recommended next action

Run a bounded direct neural follow-up on a small MLP or GPT-2-small-class model comparing dense, top-k gradient error feedback, top-k delta, and stabilized delta feedback under equal byte budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural validation of top-k gradient delta encoding under equal byte budgets
- Success threshold: At 2-5% transmitted coordinates, top-k delta achieves within 1 percentage point validation accuracy or within 3% validation loss of dense and matches or beats top-k gradient error feedback at equal bytes without divergence across seeds.
- Stop condition: Stop if top-k delta loses more than 3 percentage points accuracy versus dense at 5% k, diverges in two or more seeds, or is consistently worse than top-k gradient error feedback at equal bytes.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-top-k-gradient-delta-encoding-for-simulated-volunteer-training-4800197d0305`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
