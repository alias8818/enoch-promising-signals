# Quality-filtered data selection for tiny pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quality-filtered-data-selection-for-tiny-pretraining-039806429081`
Run ID: `quality-filtered-data-selection-for-tiny-pretraining-039806429081-20260621T085457906431+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/094f0ceaee0d

## What looked useful

Quality-top selection increased selected clean fraction from 0.512 to 0.814 and improved clean validation loss from 1.996 to 1.793 mean nats/token across three seeds. Quality-bottom selected 0.000 clean fraction and degraded clean loss to 4.337. Quality-top worsened noisy validation loss from 2.746 to 4.391, showing a domain-coverage tradeoff.

## Boundaries and scale limits

Three seeds, synthetic template/corruption corpus, character-level 2-layer Transformer, 450-document selections, 250 training steps; no real web corpus, tokenizer-level model, GPT-2-small-class baseline, downstream task, or long-run validation.

## Claim scope

In a synthetic mixed clean/noisy corpus for character-level tiny causal LM pretraining, a simple observable quality filter improved clean validation loss under a fixed document budget compared with random selection, while hurting noisy-domain validation loss.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is proxy-only for real data selection and therefore insufficient for a paper-ready claim.

## Recommended next action

Stop this run as a no-paper useful signal; next run should repeat the same four-policy design on a small real text corpus with a documented quality score and tokenizer-level tiny LM.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus quality filtering for tokenizer-level tiny pretraining
- Success threshold: Quality-top improves clean held-out loss by at least 5% relative to random at matched sequence-item budget without catastrophic degradation on the noisy/domain-shifted validation set, and quality-bottom is worse than random on clean loss.
- Stop condition: Stop if quality-top fails to improve clean held-out loss versus random in two independent seeds, or if gains vanish after matching token count and document length distributions.

## Evidence references

- Artifact root: `<local-path>/projects/quality-filtered-data-selection-for-tiny-pretraining-039806429081`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
