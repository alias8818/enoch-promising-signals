# Live CPU DDP/Gloo gradient audit with quarantine

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-cpu-ddp-gloo-gradient-audit-with-quarantine-ebe3020534`
Run ID: `live-cpu-ddp-gloo-gradient-audit-with-quarantine-ebe3020534-20260621T074352656127+0000`

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

- Parent run decision: CPU gradient audit swarm for volunteer DDP training: enoch://control-plane/projects/cpu-gradient-audit-swarm-for-volunteer-ddp-training-dbed02076d79/runs/cpu-gradient-audit-swarm-for-volunteer-ddp-training-dbed02076d79-20260621T070312168953+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f1a51ae95934

## What looked useful

Clean DDP remained finite; baseline DDP/Gloo bucket corruption produced 8 non-finite synchronized-gradient records and 8 non-finite parameter records; the quarantine comm hook detected exactly one corrupt rank-step, reported healthy count 1 at the corrupt step, and produced 0 non-finite synchronized-gradient or parameter records.

## Boundaries and scale limits

Only 2 ranks, one host, one tiny model, one corruption type, one corrupt step, and one PyTorch/Gloo version were tested. No multi-node run, larger multi-bucket model, repeated-fault sweep, overhead measurement, threshold false-positive study, or optimizer-state recovery test was performed.

## Claim scope

On a single CPU host with PyTorch 2.12.1+cpu, two DDP/Gloo ranks, a tiny model, and one synthetic rank-local gradient-bucket non-finite injection, a DDP communication-hook audit can quarantine the corrupt bucket before Gloo averaging and keep synchronized gradients and final parameters finite.

## Why it stopped

Tier 1 direct test met the scoped mechanism threshold, but evidence remains synthetic and too small for publication readiness.

## Recommended next action

Run a bounded 4-rank CPU/Gloo deepen test with a larger multi-bucket model, repeated corrupt-rank patterns, clean false-positive checks, and measured hook overhead before considering any paper-oriented claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Four-rank multi-bucket DDP/Gloo quarantine robustness and overhead check
- Success threshold: Across at least 3 seeds, quarantine prevents all injected non-finite bucket corruptions from reaching synchronized gradients/parameters, produces zero false quarantines on clean runs, and adds less than 25% wall-clock overhead versus standard clean DDP in the bounded CPU test.
- Stop condition: Stop as negative if any injected corruption reaches synchronized gradients/parameters, if clean runs trigger false quarantine under a reasonable threshold, or if overhead exceeds 25% in the bounded CPU test.

## Evidence references

- Artifact root: `<local-path>/projects/live-cpu-ddp-gloo-gradient-audit-with-quarantine-ebe3020534`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
