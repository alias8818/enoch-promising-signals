# Prompt-Internal Recurrent N-gram Speculative Decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `prompt-internal-recurrent-n-gram-speculative-decoding-eb18bb1c375c`
Run ID: `prompt-internal-recurrent-n-gram-speculative-decoding-eb18bb1c375c-20260620T054552183198+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b56f6cbef347

## What looked useful

The mechanism is a viable draft source when prompt suffixes recur, but benefit is sensitive to corpus and draft length. Long drafts can erase gains through verification overhead even when they accept slightly more bytes.

## Boundaries and scale limits

No target language model, tokenizer-level integration, KV-cache behavior, GPU timing, batching, or production speculative-decoding loop was tested. Corpora were local project text plus deterministic synthetic recurrence; one replay JSONL corpus was too small for the configured window.

## Claim scope

A bounded model-free byte-level benchmark shows that prompt-internal recurrent n-gram drafts can reduce oracle verification iterations on locally repetitive text. Best observed mean speedup proxy was 1.156 on project documentation with n=4,draft=4 and 1.447 on a deterministic synthetic recurrent corpus with n=4,draft=8.

## Why it stopped

No-paper proxy closure: this run produced direct mechanism evidence but not direct model-throughput validation.

## Recommended next action

Implement the same n-gram drafter inside a real small-model greedy decoding loop and compare exact-output wall-clock tokens/sec, acceptance rate, and generated-token equivalence against baseline greedy decoding and a prompt-lookup control.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model recurrent n-gram speculative decoding wall-clock validation
- Success threshold: At least 1.10x mean wall-clock tokens/sec improvement on repeated prompts with exact output preservation and no more than 2% slowdown on non-repeated prompts.
- Stop condition: Stop if exact output preservation fails, mean repeated-prompt speedup is below 1.05x after adaptive tuning, or non-repeated prompts slow down by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/prompt-internal-recurrent-n-gram-speculative-decoding-eb18bb1c375c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
