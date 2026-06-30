# Grammar-matched controls for predictive memory associative recall

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `grammar-matched-controls-for-predictive-memory-associative-55958acf89`
Run ID: `grammar-matched-controls-for-predictive-memory-associative-55958acf89-20260620T073531646351+0000`

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

- Parent run decision: Predictive Operator-Model Memory Updates: enoch://control-plane/projects/predictive-operator-model-memory-updates-512071ff306f/runs/predictive-operator-model-memory-updates-512071ff306f-20260620T065702032104+0000
- Parent run decision: Predictive memory operators against parameter-matched sequence-model controls: enoch://control-plane/projects/predictive-memory-operators-against-parameter-matched-sequ-b8f7f9652b/runs/predictive-memory-operators-against-parameter-matched-sequ-b8f7f9652b-20260620T071726119966+0000

## What looked useful

Grammar-mismatched controls can create false-positive predictive recall: the bigram baseline reached 100% top-1 on mismatched controls even with subject ablation but 0% top-1 on grammar-matched controls. The Transformer reached 100% top-1 on grammar_matched_64 with the subject cue and dropped to 1.7% under subject ablation.

## Boundaries and scale limits

Synthetic generated grammar only; 96 associations, three seeds, small 279k-parameter Transformer, in-distribution template draws. No natural-language corpus, pretrained/GPT-2-small-class model, long-context setting, free-form generation, or broad robustness validation.

## Claim scope

In a fixed-seed synthetic associative recall task with generated grammar templates, grammar-matched object controls separate genuine subject-target recall from grammar/category shortcuts: a bigram grammar baseline scores perfectly against mismatched decoys even without the subject cue, while a trained Transformer and explicit retrieval baseline solve grammar-matched recall only when the subject cue is present.

## Why it stopped

Medium synthetic confirmation supports the mechanism but is not publication-grade direct evidence for broad predictive-memory recall claims.

## Recommended next action

Stop this run as no-paper useful signal; next, test the same matched-vs-mismatched protocol on a GPT-2-small-class or pretrained causal LM with held-out templates and distractor facts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Grammar-matched recall controls on GPT-2-small-class associative corpora
- Success threshold: Across at least three fixed seeds, the neural model should exceed 50% top-1 on grammar-matched 64-way recall with subject cue, fall by at least 40 percentage points under subject/shuffled-association ablation, and show that n-gram/local baselines fail on grammar-matched controls despite high mismatched-control scores.
- Stop condition: Stop if the neural model does not beat n-gram/local baselines on grammar-matched 64-way recall or if subject/shuffled ablations do not substantially reduce performance.

## Evidence references

- Artifact root: `<local-path>/projects/grammar-matched-controls-for-predictive-memory-associative-55958acf89`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
