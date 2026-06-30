# Natural-language operator doctrine extraction benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `natural-language-operator-doctrine-extraction-benchmark-1906bda224`
Run ID: `natural-language-operator-doctrine-extraction-benchmark-1906bda224-20260610T203200121699+0000`

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

- Parent run decision: Operator-Doctrine Extraction vs Fact-Only Memory: enoch://control-plane/projects/operator-doctrine-extraction-vs-fact-only-memory-aa3298e77274/runs/operator-doctrine-extraction-vs-fact-only-memory-aa3298e77274-20260610T194029429654+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bc2b9d07cee3

## What looked useful

The benchmark design is useful for exposing template overfitting: the schema-aware rule baseline scored 1.0000 field accuracy on template cases but only 0.1389 on held-out paraphrases, failing the predeclared 0.85 overall field-accuracy threshold at 0.8278.

## Boundaries and scale limits

Small authored corpus only: 32 template cases and 8 held-out paraphrases, no real programming-language manual excerpts, no LLM or trained extractor evaluation, and no human annotation agreement study.

## Claim scope

Controlled 40-case Tier 1 benchmark of 9-field operator doctrine extraction from authored natural-language operator descriptions using deterministic regex and schema-aware rule baselines.

## Why it stopped

Controlled small direct test failed the predeclared schema-aware baseline threshold, mainly because held-out paraphrases exposed cue-pattern brittleness; this is an early direct falsification of the simple benchmark/extractor success threshold, not a full real-world validation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should evaluate a blind held-out paraphrase plus real-doc excerpt split with an extractor that was not written against the generation templates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Blind held-out and real-doc operator doctrine extraction
- Success threshold: On the blind combined split, extractor overall field accuracy >= 0.85, exact-case accuracy >= 0.60, and no individual semantic field below 0.70 accuracy.
- Stop condition: Stop if blind held-out plus real-doc field accuracy remains below 0.75 or annotation disagreement shows the doctrine schema is unstable for real documentation.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-operator-doctrine-extraction-benchmark-1906bda224`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
