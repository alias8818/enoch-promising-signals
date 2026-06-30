# N-Gram Suffix Speculative Decoding on CPU with Exact No-Spec Baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-speculative-decoding-on-cpu-with-exact-no-spec-baseline-e65f5c458f8a`
Run ID: `n-gram-suffix-speculative-decoding-on-cpu-with-exact-no-spec-baseline-e65f5c458f8a-20260621T102622741319+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bd2d277891e5

## What looked useful

Exactness held in 36/36 configurations and median target-call ratio fell to 0.265625, but median wall-clock speedup was only 0.7063 and the best observed speedup was 0.8861, so call reduction alone was insufficient under this local CPU proxy.

## Boundaries and scale limits

Proxy-only evidence: no real transformer LM, no real tokenizer, no KV-cache implementation, four short prompts, 192 generated tokens per prompt, and synthetic target-call CPU cost.

## Claim scope

In a bounded NumPy CPU proxy with a deterministic copy-biased target model, n-gram suffix speculative decoding preserved exact greedy output and reduced target-call count, but did not improve wall-clock time versus an exact no-spec baseline.

## Why it stopped

Proxy/local evidence supports exactness but not wall-clock speedup; this is not a full validation on a real language model.

## Recommended next action

Stop this run as a proxy early falsification of the CPU speedup claim; the concrete next bounded test is a real small-transformer CPU implementation with exact greedy equivalence and KV-cache-aware verification.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer CPU n-gram suffix speculative decoding with exact greedy baseline
- Success threshold: All outputs exactly match no-spec greedy; median wall-clock speedup is greater than 1.10; no prompt class has median speedup below 0.95.
- Stop condition: Stop if exactness fails, or if a correct KV-cache-aware implementation remains at or below 1.00 median speedup after bounded ablations.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-speculative-decoding-on-cpu-with-exact-no-spec-baseline-e65f5c458f8a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
