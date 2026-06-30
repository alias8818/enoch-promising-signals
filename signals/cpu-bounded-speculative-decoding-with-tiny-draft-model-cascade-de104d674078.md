# CPU-bounded Speculative Decoding with Tiny Draft Model Cascade

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-bounded-speculative-decoding-with-tiny-draft-model-cascade-de104d674078`
Run ID: `cpu-bounded-speculative-decoding-with-tiny-draft-model-cascade-de104d674078-20260526T014830968302+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/09eea6a20198

## What looked useful

The cascade mechanism improved over a single tiny draft by raising acceptance from about 66% to 87%. Single-draft speculative decoding stayed below baseline, while the two-stage cascade crossed break-even only at wide verification blocks, reaching 1.23x at gamma=16 with exact output matching.

## Boundaries and scale limits

Not a real LLM, not a real learned draft cascade, and not a production CPU serving stack; target cost is a dense NumPy projection and draft cost is under-modeled as table lookup. No 7B-scale, prompt-suite, KV-cache, or tokenizer evidence was produced.

## Claim scope

Controlled synthetic CPU proxy for deterministic greedy decoding: a two-stage tiny-draft cascade with cheap lookup drafts, 87% acceptance, and gamma=16 preserved exact output and averaged 1.23x greedy baseline throughput over five seeds.

## Why it stopped

Proxy evidence supports the mechanism but is not direct enough for a paper; this run stops as a no-paper useful signal rather than claiming real-model validation.

## Recommended next action

Run a bounded real-model CPU follow-up using a small transformer target and two actual tiny draft models; require exact distribution/greedy equivalence checks and compare gamma 8, 12, and 16 against greedy baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Small-LM CPU Test of Two-Stage Tiny Draft Cascade
- Success threshold: At least 1.15x greedy baseline throughput on mean and median prompt-suite results with exact output or valid speculative sampling equivalence, plus target calls/token below 0.20 and measured draft overhead below the saved target time.
- Stop condition: Stop if acceptance stays below 80%, draft overhead erases target-call savings, or gamma 16 cannot preserve correctness/practical latency on CPU.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-bounded-speculative-decoding-with-tiny-draft-model-cascade-de104d674078`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
