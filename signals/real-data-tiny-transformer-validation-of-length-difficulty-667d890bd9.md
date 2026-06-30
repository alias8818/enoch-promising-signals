# Real-data tiny-Transformer validation of length-difficulty balanced selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-data-tiny-transformer-validation-of-length-difficulty-667d890bd9`
Run ID: `real-data-tiny-transformer-validation-of-length-difficulty-667d890bd9-20260608T211844563008+0000`

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

- Parent run decision: Length-Difficulty Balanced Data Selection for Tiny Pretraining: enoch://control-plane/projects/length-difficulty-balanced-data-selection-for-tiny-pretraining-48d0635d3544/runs/length-difficulty-balanced-data-selection-for-tiny-pretraining-48d0635d3544-20260608T174925967853+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/7039c70da27b

## What looked useful

Joint length+difficulty balancing beat random on mean validation loss in all paired main and confirmation seeds and beat length-only and difficulty-only controls in the 1000-step confirmation. The effect size was small: about 0.47% overall validation-loss improvement and 0.49% long+hard-bin improvement versus random in the confirmation run, below the 1% success threshold.

## Boundaries and scale limits

Limited to WikiText-2, first 4500 training documents and 700 validation documents, subset size 540, sequence length 64, tiny 2-layer 96-dim Transformer, up to 1000 optimizer steps, and five seeds. No GPT-2-small-class baseline, larger corpus, downstream transfer, or long training validation was run.

## Claim scope

On WikiText-2 with a word-level tiny causal Transformer, same-size length+difficulty balanced document selection produced a consistent directional validation-loss improvement over random selection across paired small-run seeds, but the improvement was below the predeclared 1% practical threshold.

## Why it stopped

Tier-1 direct evidence was useful but below the stated success threshold, so this should remain no-paper evidence rather than a positive validation.

## Recommended next action

Run a bounded deepen test on two real corpora with larger selected subsets and at least five paired seeds; stop if joint balancing again fails to reach >=1% validation-loss reduction without hard-bin regression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-corpus bounded confirmation of length+difficulty balanced selection
- Success threshold: Joint length+difficulty balancing must reduce mean validation cross-entropy by >=1% versus random on both corpora and must not increase the long+hard-bin loss versus random; it should also beat length-only and difficulty-only controls on average.
- Stop condition: Stop as a no-paper negative if either corpus fails the >=1% paired validation-loss threshold or if the long+hard bin regresses versus random.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-tiny-transformer-validation-of-length-difficulty-667d890bd9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
