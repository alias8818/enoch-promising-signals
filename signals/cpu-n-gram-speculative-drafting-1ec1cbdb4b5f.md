# CPU N-gram Speculative Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-n-gram-speculative-drafting-1ec1cbdb4b5f`
Run ID: `cpu-n-gram-speculative-drafting-1ec1cbdb4b5f-20260608T031410517454+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de208cd5fa47

## What looked useful

Python stdlib code reached 0.95678 proposal coverage, 0.43534 first-token acceptance per proposal, and 1.39224 accepted tokens per evaluated position at roughly 268k positions/s with under 190 MB RSS; Gutenberg prose reached only 0.15236 accepted tokens per position.

## Boundaries and scale limits

No live target LLM, no verifier batching, no KV-cache measurement, no quality evaluation, and only one natural-prose corpus plus local Python stdlib code were tested.

## Claim scope

Bounded proxy evidence on 120k-token cl100k_base slices shows CPU n-gram speculative drafting is cheap and can recover useful exact continuations for repetitive/code-like text, but not broad natural prose.

## Why it stopped

Closed as no-paper useful signal because current evidence is an offline exact-match proxy, not direct target-model speculative decoding validation.

## Recommended next action

Run a bounded live small-model speculative decoding test on code-completion prompts to determine whether the proxy acceptance translates into end-to-end tokens/s speedup.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live small-model validation of CPU n-gram drafting on code prompts
- Success threshold: At least 10% end-to-end tokens/s improvement on code prompts with unchanged greedy outputs and no more than 5% slowdown on prose prompts.
- Stop condition: Stop if accepted draft tokens per step are below 0.5 on code prompts or end-to-end throughput does not exceed baseline after verifier overhead.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-n-gram-speculative-drafting-1ec1cbdb4b5f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
