# Static Corpus N-gram Draft Tree on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `static-corpus-n-gram-draft-tree-on-cpu-a7311c4910ba`
Run ID: `static-corpus-n-gram-draft-tree-on-cpu-a7311c4910ba-20260604T131418862849+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/34c67bd6c0ac

## What looked useful

Byte-level static n-gram trees show a real in-domain prefix-coverage mechanism, but word-level exact n-gram matching collapses from context sparsity. The result motivates tokenizer-matched verification before any practical speculative-decoding claim.

## Boundaries and scale limits

Single public 1.06 MiB corpus, 80/20 in-domain split, exact byte/whitespace-word tokenization, 5,000 sampled held-out positions, no target LLM verifier, no BPE tokenizer, no serving throughput measurement.

## Claim scope

On Tiny Shakespeare held-out text, a static byte-level n-gram draft tree can cover the next byte with 85.04% coverage and average 2.54 accepted bytes at context length 4, branch 8, depth 8; exact word-level n-gram trees are sparse and weak, with best mean accepted continuation only 0.26 words.

## Why it stopped

No-paper useful signal: this is a proxy/early falsification of the stronger static corpus n-gram CPU draft-tree claim, not a full validation.

## Recommended next action

Run a bounded BPE-tokenized small-LLM verifier test and require wall-clock tokens/s plus accepted model tokens per step before considering this idea further.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE-tokenized static n-gram draft tree with small LLM verifier
- Success threshold: At branch/depth bounded to no more than 64 draft nodes, show >=1.5 accepted BPE tokens per verifier step and >=10% end-to-end tokens/s improvement over the best baseline on 5,000 held-out positions.
- Stop condition: Stop if BPE mean accepted tokens is <1.0 or if CPU tree overhead removes any measured verifier-throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/static-corpus-n-gram-draft-tree-on-cpu-a7311c4910ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
