# Small-LM Direct Validation of Online Suffix-Automaton Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-lm-direct-validation-of-online-suffix-automaton-draf-d98a7618c4`
Run ID: `small-lm-direct-validation-of-online-suffix-automaton-draf-d98a7618c4-20260630T111503558942+0000`

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

- Parent run decision: Prompt+KV Suffix-Automaton N-gram Speculative Decoding: enoch://control-plane/projects/prompt-kv-suffix-automaton-n-gram-speculative-decoding-6e9005865c96/runs/prompt-kv-suffix-automaton-n-gram-speculative-decoding-6e9005865c96-20260630T103803235906+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/e3b49e3a046a

## What looked useful

Suffix-copy drafting accepted 82.0% of proposed tokens with 99.1% coverage on synthetic repeated motifs, but only 5.6% of proposed tokens with 86.6% coverage on WikiText. Requiring 8-token contexts raised WikiText token acceptance to 39.2% but reduced coverage to 1.16%. GPT-2 sampled first-token accuracy on WikiText was 34.4%, above the default suffix-copy first-token hit rate of 23.9% when proposed.

## Boundaries and scale limits

This run used a bounded suffix-context index rather than a full suffix automaton, 50k-token corpora, one WikiText natural-text split, and a sampled GPT-2 first-token baseline. It did not measure end-to-end target-model speculative decoding speed.

## Claim scope

A bounded online suffix-context copy drafter was evaluated on 50k-token synthetic repeated motifs and 50k GPT-2-token WikiText-2 natural text. It is effective on exact-repeat synthetic streams but weak as a broad natural-text drafter.

## Why it stopped

Proxy/direct bounded validation found a mixed mechanism: strong on exact repeats, weak for broad WikiText natural text. This is not a full validation and not paper-positive.

## Recommended next action

Run a bounded deepen experiment on repeat-heavy real corpora with a true online suffix automaton and end-to-end target-model speculative decoding timing; stop this broad natural-text validation as no-paper useful signal.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end suffix-automaton drafting on repeat-heavy real corpora
- Success threshold: At least 1.10x end-to-end throughput over no-draft decoding on a repeat-heavy real corpus, with accepted-token rate above 20% and proposal coverage above 10%, while not regressing the natural-text control interpretation.
- Stop condition: Stop if repeat-heavy real corpora show below 10% proposal coverage or below 10% accepted-token rate at practical draft lengths, or if verifier timing shows no throughput gain.

## Evidence references

- Artifact root: `<local-path>/projects/small-lm-direct-validation-of-online-suffix-automaton-draf-d98a7618c4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
