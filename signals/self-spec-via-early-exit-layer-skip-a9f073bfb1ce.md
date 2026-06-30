# Self-Spec via Early-Exit Layer Skip

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `self-spec-via-early-exit-layer-skip-a9f073bfb1ce`
Run ID: `self-spec-via-early-exit-layer-skip-a9f073bfb1ce-20260628T132258640775+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/01cf0d500512

## What looked useful

Layer 3/6/9 exits accepted only 6.6%/11.3%/30.9% of full-model greedy tokens with accepted-token speed proxies of 0.19/0.20/0.40. Near-final layer 10/11 exits improved to 43.8%/58.6% acceptance but only 1.18x/1.08x truncated-forward speedup, leaving proxies of 0.52/0.64 before verifier overhead.

## Boundaries and scale limits

Single pretrained GPT-2-small-class model, one sequence batch, greedy top-1 proxy, no trained auxiliary heads, no end-to-end speculative decoder, no multi-model or multi-corpus robustness.

## Claim scope

For GPT-2 small on a bounded local next-token probe, untrained tied-head early exits from skipped layers do not provide a useful greedy self-speculative draft: acceptance is too low when latency speedup is meaningful, and near-final exits recover acceptance only after most of the speedup disappears.

## Why it stopped

Early local falsification of the untrained early-exit layer-skip mechanism, not a full validation across models or complete speculative decoding systems.

## Recommended next action

Stop this untrained tied-head layer-skip variant as a no-paper result; only continue with a bounded deepen test that trains or calibrates the early-exit head and requires accepted-token proxy above 1 before end-to-end decoding work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated Early-Exit Head for Self-Speculative Layer Skip
- Success threshold: On held-out text, at least one exit depth must achieve accepted-token speed proxy > 1.1 before verifier overhead and must show end-to-end greedy decoding wall-clock speedup after verifier overhead.
- Stop condition: Stop if calibrated heads cannot exceed accepted-token speed proxy 1.0 on held-out text or if end-to-end verifier overhead removes the measured proxy gain.

## Evidence references

- Artifact root: `<local-path>/projects/self-spec-via-early-exit-layer-skip-a9f073bfb1ce`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
