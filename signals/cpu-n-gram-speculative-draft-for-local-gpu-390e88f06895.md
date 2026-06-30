# CPU n-gram speculative draft for local GPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-draft-for-local-gpu-390e88f06895`
Run ID: `cpu-n-gram-speculative-draft-for-local-gpu-390e88f06895-20260525T051941441026+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/11a49bfa7e02

## What looked useful

The naive CPU n-gram drafter preserves greedy output under verification and reduces target verifier calls by about 9-10.5%, but proposed-token acceptance is only about 3-10.6% and output tokens per verifier call stays near 1.10-1.12, too weak for a practical or paper-ready local GPU speculative decoding claim.

## Boundaries and scale limits

Not a production KV-cache serving benchmark, not a 7B+ model result, not a broad corpus validation, and parallel variant timing runs should be treated as call-count/acceptance evidence rather than clean latency evidence.

## Claim scope

Bounded GB10 probe using distilgpt2 on Wikitext-2 with a CPU frequency n-gram drafter built from 200k tokenizer tokens and exact greedy GPU verification over draft lengths 1, 2, and 4.

## Why it stopped

Bounded direct probe found only weak verifier-call reduction and very low acceptance, so this is an early negative/useful-signal result rather than a full validation of CPU n-gram speculative decoding.

## Recommended next action

Stop this naive n-gram variant as no-paper useful signal; the next bounded test should add confidence-gated or prompt-local drafting and require at least 1.25 output tokens per verifier call on the same protocol before any larger run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Confidence-gated prompt-local CPU n-gram drafting
- Success threshold: At least 1.25 output tokens per verifier call on 4096 generated tokens with zero greedy-equivalence mismatches and CPU drafting below 5% of verifier wall time.
- Stop condition: Stop as negative if output tokens per verifier call remains below 1.20 or if confidence gating removes so many proposals that verifier-call reduction stays below 15%.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-draft-for-local-gpu-390e88f06895`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
