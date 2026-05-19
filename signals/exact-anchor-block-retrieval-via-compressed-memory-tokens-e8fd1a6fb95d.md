# Exact-Anchor Block Retrieval via Compressed Memory Tokens

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-block-retrieval-via-compressed-memory-tokens-e8fd1a6fb95d`
Run ID: `exact-anchor-block-retrieval-via-compressed-memory-tokens-e8fd1a6fb95d-20260518T022555123445+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/27b55e4499f7

## What looked useful

Compressed memory tokens learned partial payload information, reaching 90.1% token accuracy and 46.7% block-exact accuracy after 12k steps with one memory token, but exact retrieval remained far below the 100% oracle and slotwise control.

## Boundaries and scale limits

Toy synthetic task only; no natural-language documents, no pretrained transformer integration, no GPT-2-small-class parameter-matched baseline, one extended compressed seed, two medium seeds, maximum 12k local training steps.

## Claim scope

On a synthetic in-context benchmark with 8 random anchored blocks, 8-token payloads, 64 payload symbols, and 128 anchor keys, the tested learned compressed-memory-token models did not achieve exact block retrieval, while an oracle and an addressable slotwise control reached 100% block-exact accuracy.

## Why it stopped

Bounded synthetic evidence shows partial learning but not exact-anchor block retrieval from compressed memory tokens; this is an early local falsification of the simple exact-retrieval claim, not a full-scale validation.

## Recommended next action

Stop this run as a no-paper useful signal; a bounded follow-up should test whether a more structured compression objective can reach at least 95% exact block recovery on the same benchmark across multiple seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Structured Compression Objective for Exact Anchor Retrieval
- Success threshold: At least 95% block-exact accuracy on the 8-block, 8-token benchmark across at least 3 seeds while using fewer than 8 memory tokens per block.
- Stop condition: Stop as negative if structured compression remains below 80% block-exact accuracy after matching or exceeding the 12k-step budget used here, or if gains disappear across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-block-retrieval-via-compressed-memory-tokens-e8fd1a6fb95d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
