# Local Loss Curriculum for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-loss-curriculum-for-tiny-pretraining-b844dcdb6369`
Run ID: `local-loss-curriculum-for-tiny-pretraining-b844dcdb6369-20260526T014831408158+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6fe9efb9df68

## What looked useful

Naive hard-focus local-loss curricula can actively degrade tiny pretraining, even on explicitly hard local targets. Mild easy-to-hard weighting is not falsified but was too unstable across seeds to support a paper-ready claim.

## Boundaries and scale limits

Synthetic data only; 619,648-parameter transformer; 800 training steps; batch size 64; sequence length 64; 8 seeds only for the mild-strength confirmation; no natural-language corpus, GPT-2-small-class run, downstream transfer, or long-run convergence test.

## Claim scope

In a bounded synthetic tiny-transformer pretraining probe with rare locally hard exception tokens, aggressive local-loss weighting hurt validation loss and hard-token loss versus uniform training. A mild easy-to-hard local-loss curriculum showed only a small, seed-unstable average validation-loss improvement and no material hard-token improvement.

## Why it stopped

Proxy/tiny evidence is sufficient for a no-paper useful signal but not for full validation: aggressive local-loss weighting failed directly in the synthetic setup, while the only positive mild signal was small, seed-unstable, and did not improve hard-token loss.

## Recommended next action

Run one bounded deepen follow-up on a small real-text corpus with the mild easy-to-hard schedule, paired uniform controls, at least 8 seeds, and predeclared validation and hard-slice thresholds; otherwise stop treating naive local-loss hard-focus as promising.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mild Easy-to-Hard Local-Loss Curriculum on Small Real-Text Tiny Pretraining
- Success threshold: Mild easy_to_hard beats uniform on mean paired validation loss by at least 1 percent, wins at least 6 of 8 seeds, and does not worsen the high-loss-token validation slice by more than 0.5 percent.
- Stop condition: Stop if mild easy_to_hard wins fewer than 5 of 8 seeds, improves mean validation loss by less than 0.5 percent, or worsens the high-loss-token slice by at least 1 percent.

## Evidence references

- Artifact root: `<local-path>/projects/local-loss-curriculum-for-tiny-pretraining-b844dcdb6369`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
