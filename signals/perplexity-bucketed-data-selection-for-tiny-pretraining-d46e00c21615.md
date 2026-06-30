# Perplexity-Bucketed Data Selection for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-bucketed-data-selection-for-tiny-pretraining-d46e00c21615`
Run ID: `perplexity-bucketed-data-selection-for-tiny-pretraining-d46e00c21615-20260609T161852804385+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/000e22f99bde

## What looked useful

Perplexity buckets behave more like a difficulty/fit filter than a universally better selector: the high-perplexity tail wasted scarce tiny-LM tokens, low-perplexity filtering helped by about 1.0% PPL at 60k characters, and the effect nearly vanished at 160k characters.

## Boundaries and scale limits

Single dataset, n-gram teacher proxy, character-level student, small local token budgets, validation perplexity only; no neural teacher, BPE/GPT-2-small-class student, downstream tasks, or large-corpus pretraining.

## Claim scope

On WikiText-2 with a 352,957-parameter character-level Transformer student and a character 5-gram teacher, high-teacher-perplexity-only selection is worse than random under scarce-token tiny pretraining; low-teacher-perplexity selection gives a modest benefit at a 60k-character budget but not a robust broad improvement at 160k characters.

## Why it stopped

No paper-ready result: the local direct probe found only a modest low-perplexity filtering benefit and a clearer high-perplexity negative, with teacher/model proxies that prevent broad validation.

## Recommended next action

Run one bounded neural-teacher follow-up using BPE-tokenized WikiText-2/OpenWebText subset and a GPT-2-small-class or parameter-matched tiny student before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural-teacher perplexity buckets for BPE tiny-LM pretraining
- Success threshold: Low or high-tail-excluded selection improves validation perplexity by at least 2% versus random with paired multi-seed consistency, while high-only selection is not the best regime.
- Stop condition: Stop if the neural-teacher/BPE setup shows less than 1% mean PPL gain over random or inconsistent paired-seed direction across two budgets.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-bucketed-data-selection-for-tiny-pretraining-d46e00c21615`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
