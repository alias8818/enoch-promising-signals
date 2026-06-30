# Speculative Decoding Draft Selection: N-Gram Suffix vs Tiny LM Draft

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-draft-selection-n-gram-suffix-vs-tiny-lm-draft-b7c93d4ca1a8`
Run ID: `speculative-decoding-draft-selection-n-gram-suffix-vs-tiny-lm-draft-b7c93d4ca1a8-20260612T225843892064+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e67206aaa6d

## What looked useful

Suffix n-gram drafting is a strong cheap baseline: at 1000 GRU steps, suffix n-gram reached 0.210 first-token match and 0.265 mean accepted prefix versus tiny GRU 0.205 and 0.255, with roughly 138x lower draft-generation time. Both methods had low absolute acceptance, so this is no-paper evidence.

## Boundaries and scale limits

Proxy-only greedy acceptance; distilgpt2 target; 80k training tokens; 200 validation contexts in the strongest run; compact GRU draft rather than a tuned transformer; no production speculative verification batching or end-to-end serving throughput.

## Claim scope

On WikiText-2 validation contexts with a distilgpt2 greedy target, a suffix n-gram draft matched or slightly exceeded a 1000-step tiny GRU draft in first-token target agreement and mean accepted greedy prefix length, while drafting far faster in the local implementation.

## Why it stopped

Closed as no-paper useful signal: the local proxy supports suffix n-gram as a cheap baseline but shows low absolute accepted-token yield and lacks direct serving-throughput evidence.

## Recommended next action

Run a bounded direct speculative-decoding implementation with probability-correct acceptance and batched target verification before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct batched speculative decoding test for suffix n-gram versus tuned tiny transformer draft
- Success threshold: Suffix n-gram is at least 1.2x faster end-to-end than the tiny neural draft on repetition-heavy prompts without lower acceptance quality, or the neural draft clearly exceeds suffix n-gram by at least 20% accepted tokens per second overall.
- Stop condition: Stop if both methods remain below 0.5 mean accepted tokens per draft or if batched verification eliminates any end-to-end speed advantage.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-draft-selection-n-gram-suffix-vs-tiny-lm-draft-b7c93d4ca1a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
