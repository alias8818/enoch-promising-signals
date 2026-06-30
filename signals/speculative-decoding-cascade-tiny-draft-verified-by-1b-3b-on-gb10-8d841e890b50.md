# Speculative decoding cascade: tiny draft verified by 1B+3B on gb10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-cascade-tiny-draft-verified-by-1b-3b-on-gb10-8d841e890b50`
Run ID: `speculative-decoding-cascade-tiny-draft-verified-by-1b-3b-on-gb10-8d841e890b50-20260621T170903581667+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/02abaca87fa0

## What looked useful

The cascade mechanism can reduce final-verifier candidate work without changing deterministic 3B output, but the added 1B-class verifier overhead outweighed saved 3B work in this local implementation. Standard 0.5B->3B speculative decoding was faster.

## Boundaries and scale limits

Only 4 prompts and 256 generated tokens in the larger direct run; full-context recomputation rather than production KV-cache scheduling; greedy decoding only; no batching, no pipeline overlap, no stochastic sampling, and no serving-system integration.

## Claim scope

On GB10 with a serial Python Transformers harness and Qwen2.5 0.5B/1.5B/3B greedy decoding, a 1.5B intermediate verifier preserved exact 3B greedy output and reduced 3B candidate verifier positions by about 30-33% versus direct 0.5B->3B speculative verification, but did not improve wall-clock throughput.

## Why it stopped

Direct bounded GB10 evidence is mixed: exactness and target-candidate reduction are supported, but practical wall-clock speedup is negative in the tested implementation.

## Recommended next action

Stop this run as no-paper useful signal; only revisit with a KV-cache-aware serving prototype that can test whether target-work reduction translates to throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache-aware cascade speculative decoding serving prototype
- Success threshold: Cascade must preserve exact 3B greedy output and improve end-to-end tokens/s by at least 10% over standard 0.5B->3B speculative decoding while reducing 3B verifier positions/token.
- Stop condition: Stop if a cache-aware prototype remains slower than standard speculative decoding after confirming exactness and comparable prompt/output workload.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-cascade-tiny-draft-verified-by-1b-3b-on-gb10-8d841e890b50`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
