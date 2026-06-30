# Suffix-Tree Draft Model Acceptance Probe

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-draft-model-acceptance-probe-c4920757e2fe`
Run ID: `suffix-tree-draft-model-acceptance-probe-c4920757e2fe-20260621T144012061679+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/14825ec65079

## What looked useful

Five-seed synthetic runs show suffix-context acceptance fraction 0.7171 on shared repeated motifs versus 0.6889 for ngram_4, but 0.0735 on low-order Markov versus 0.1152 for ngram_2 and near-zero transfer on held-out motifs.

## Boundaries and scale limits

Tested only standard-library CPU synthetic corpora up to 50k train tokens and 10k test tokens across five seeds, with horizon 8 and max suffix context 24. No neural target model, real tokenizer trace, compressed suffix tree, GPU path, or end-to-end speculative decoding latency was tested.

## Claim scope

On synthetic token streams, a suffix-context draft acceptor improves exact multi-token acceptance over fixed n-gram baselines when train and test share repeated long motifs, but it does not provide general acceptance gains across low-order Markov or held-out motif regimes.

## Why it stopped

Synthetic proxy evidence is mixed: suffix-context helps repeated shared motifs but fails to generalize and is not direct full validation of model-serving acceptance.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use real LLM/GPT-2-small token traces and compare accepted tokens per verification call plus memory/lookup cost against n-gram and prompt-cache baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-level suffix-context draft acceptance on GPT-2-small-class continuations
- Success threshold: Suffix-context improves accepted tokens per verification call by at least 5% over the best baseline on repeated real traces while staying within 2x baseline lookup latency and showing no claimed gain on held-out controls.
- Stop condition: Stop if suffix-context does not beat the best baseline by 5% on repeated real traces, if lookup/memory overhead dominates the acceptance gain, or if gains disappear under held-out/control splits.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-draft-model-acceptance-probe-c4920757e2fe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
